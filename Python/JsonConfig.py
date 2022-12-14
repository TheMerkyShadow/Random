import os
import sys

import json

from pathlib import Path

class JsonConfig:
    def __init__(self, dir='/'):
        self.Path = Path(dir)
        self.Decode()
    def Decode(self):
        self.Table = json.loads(self.Path.read_text())
    def Encode(self):
        return json.dumps(self.Table, indent=4)
    def __getitem__(self, item):
        return self.Table.get(item, None)
    def __setitem__(self, item, value):
        if item in self.Table:
            self.Table[item] = value
    def Write(self):
        self.Path.write_text(self.Encode())
    def __repr__(self) -> str:
        return repr(self.Table)
