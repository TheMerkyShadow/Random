import os
import sys

import json

from pathlib import Path

class JsonConfig:
    def __init__(self, dir='manifest.json'):
        self.Path = Path(dir)
        self.Check()
        self.Decode()
    def Check(self):
        if not self.Path.exists():
            self.Path.write_text("{}")
    def Decode(self):
        self.Table = json.loads(self.Path.read_text())
        return self.Table
    def Encode(self):
        return json.dumps(self.Table, indent=4)
    def __getitem__(self, item):
        try:
            return self.Table[item]
        except Exception as e:
            return None
    def __setitem__(self, item, value):
        self.Table[item] = value
        self.Write()
    def __delitem__( self, value ):
        self.Table.pop(value)
        self.Write()  
    def Write(self):
        self.Path.write_text(self.Encode())
