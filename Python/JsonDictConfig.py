import os
import sys

import json

from pathlib import Path

class JsonDictConfig:
    
    """
    A class for managing JSON configuration data stored in a file.

    Example usage:
    # Initialize the configuration object with the default file path 'config.json'
    config = JsonDictConfig()

    # Access configuration settings
    print(config['key'])  # Example: Accessing a specific key in the configuration

    # Modify configuration settings
    config['new_key'] = 'new_value'  # Example: Adding a new key-value pair to the configuration

    # Save the modified configuration to the file
    config.Write()

    # Delete an item from the configuration
    del config['key_to_delete']

    # Clear the entire configuration
    config.Destroy()
    """
    
    def __init__(self, dir='config.json'):
        self.Path = Path(dir)
        self.Path.touch(exist_ok=True) 
        self.Read() 
    def Read(self):
        self.Table = json.loads(self.Path.read_text())
    def Encode(self):
        return json.dumps(self.Table, indent=4)
    def __getitem__(self, item):
        return self.Table.get(item, None)
    def __setitem__(self, item, value):
        self.Table[item] = value
    def __delitem__(self, item):
         if item in self.Table:
              del self.Table[item]   
             
    def Write(self):
        self.Path.write_text(self.Encode())
    def Destroy(self):
        self.Table = {}
        self.Write()
    def __repr__(self):
        return repr(self.Table)
