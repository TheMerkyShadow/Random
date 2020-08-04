import os
import sys

import json

from pathlib import Path

class JsonConfig:
    def __init__(self, dir='manifest.json'):
        self.Path = Path(dir)
        self.Decode()
    def Decode(self):
        self.Table = json.loads(self.Path.read_text())
        return self.Table
    def Encode(self):
        return json.dumps(self.Table, indent=4)
    def __getitem__(self, item):
        return self.Table[item]
    def __setitem__(self, item, value):
        self.Table[item] = value
        self.Write()
    def Write(self):
        self.Path.write_text(self.Encode())
