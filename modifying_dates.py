"""
Helper to change both creation and modification dates of every file inside input directory
"""

from win32_setctime import setctime
from pathlib import Path
import os
from datetime import datetime

from main import depth_first_search, INPUTDIR


def modify_date(path: Path):
    day, month, year, *_ = map(int, path.name.split('\\')[-1].split('.')[0].split('-'))
    DATE = datetime(year, month, day).timestamp()
    os.utime(path, (DATE, DATE))
    setctime(path, DATE)


def modify_dates():
    [modify_date(file.path) for file in depth_first_search(INPUTDIR)]

modify_dates()