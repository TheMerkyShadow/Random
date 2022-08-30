import os
import sys
import time

from pathlib import Path

from tkinter import *
from tkinter.filedialog import askopenfilenames

files = askopenfilenames(initialdir=os.getcwd())
if files:
    for filename in files:
        file = Path(filename)

        # Apply Rule Here
        rule = filename.lower()

        file.rename( rule )
