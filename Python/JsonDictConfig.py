import os
import sys

import json

from pathlib import Path

class JsonDictConfig:
    def __init__(self, dir='config.json'):
        self.Path = Path(dir)
        self.Read() 
    def Read(self):
        self.Table = json.loads(self.Path.read_text())
    def Encode(self):
        return json.dumps(self.Table, indent=4)
    def __getitem__(self, item):
        return self.Table.get(item, None)
    def __setitem__(self, item, value)
        self.Table.setdefault(item, value)    
    def __delitem__(self, item):
         if item in self.Table:
              del self.Table[item]        
    def Write(self):
        self.Path.write_text(self.Encode())
    def __repr__(self) -> str:
        return repr(self.Table)
