import os
import sys
import time
import socket
import atexit
import json
import tkinter as tk
from tkinter import filedialog, simpledialog
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import miniupnpc
import logging

logging.getLogger('pyftpdlib').disabled = True

# --- Hardcoded usernames and other settings ---
FTP_PORT = 55555
PASSIVE_PORTS = range(60000, 60010)
current_port, current_upnp = None, None

# --- LAN IP ---
def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

# --- UPnP setup ---
def setup_upnp(port, passive_ports):
    global current_port, current_upnp
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 200
    try:
        upnp.discover()
        upnp.selectigd()
        lan_ip = get_lan_ip()

        if not upnp.addportmapping(port, 'TCP', lan_ip, port, 'Python FTP Server', ''):
            raise Exception(f"[UPNP ERROR] Could not forward port {port}")
        print(f"[UPNP] Port {port} forwarded")

        for p in passive_ports:
            upnp.addportmapping(p, 'TCP', lan_ip, p, 'Python FTP Passive', '')

    except Exception as e:
        print(f"[UPNP ERROR] {e}")
        time.sleep(5)
        sys.exit(1)

    current_port, current_upnp = port, upnp
    return upnp

def cleanup_upnp():
    global current_port, current_upnp
    if current_port and current_upnp:
        try:
            current_upnp.deleteportmapping(current_port, 'TCP')
            for p in PASSIVE_PORTS:
                current_upnp.deleteportmapping(p, 'TCP')
            print(f"[UPNP CLEANUP] Removed forwarded ports")
        except:
            pass

atexit.register(cleanup_upnp)

# --- FTP Handler ---
class MaxSpeedFTPHandler(FTPHandler):
    throttle = 0
    max_chunk_size = 1024*64

    def ftp_PORT(self, line):
        self.respond("502 Active mode not supported. Use passive mode.")

    def on_connect(self):
        print(f"[CONNECT] {self.remote_ip}:{self.remote_port} connected")

    def on_disconnect(self):
        print(f"[DISCONNECT] {self.remote_ip}:{self.remote_port} disconnected")

    def on_file_sent(self, file):
        print(f"[UPLOAD DONE] {file} to {self.remote_ip}")

    def on_file_received(self, file):
        print(f"[DOWNLOAD DONE] {file} from {self.remote_ip}")

# --- Load or create config ---
def load_config():
    CONFIG_FILE = "config.json"
    DEFAULT_CONFIG = {}
    if not os.path.exists(CONFIG_FILE):
        DEFAULT_CONFIG["folder"] = filedialog.askdirectory(title="Choose folder to share via FTP")
        DEFAULT_CONFIG["admin_pass"] = simpledialog.askstring("Admin Password","Enter admin password:",initialvalue="Admin4321")
        DEFAULT_CONFIG["guest_pass"] = simpledialog.askstring("Guest Password","Enter guest password:",initialvalue="Test1234")
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print(f"[CONFIG] Created default config.json")
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        return config

# --- Main ---
def main():
    config = load_config()

    # Authorizer
    authorizer = DummyAuthorizer()
    authorizer.add_user("admin", config["admin_pass"], config["folder"], perm="elradfmw")
    authorizer.add_user("guest", config["guest_pass"], config["folder"], perm="elr")

    # Handler and server
    handler = MaxSpeedFTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = PASSIVE_PORTS

    # LAN IP and UPnP
    lan_ip = get_lan_ip()
    upnp = setup_upnp(FTP_PORT, PASSIVE_PORTS)

    # Public IP for passive mode
    public_ip = upnp.externalipaddress()
    handler.masquerade_address = public_ip

    print(f"[SERVER] LAN IP: {lan_ip}:{FTP_PORT}")
    print(f"[SERVER] FTP accessible externally: ftp://{public_ip}:{FTP_PORT}/")

    server = FTPServer((lan_ip, FTP_PORT), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
