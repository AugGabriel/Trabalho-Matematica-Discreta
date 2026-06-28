from win32_setctime import setctime
import os
from datetime import datetime

from main import SIMPATH


def modify_date():
    PATH = os.path.join(SIMPATH, "downloads/15-12-2025.avif")
    DATE = datetime(2025, 12, 15).timestamp()
    os.utime(PATH, (DATE, DATE))
    setctime(PATH, DATE)

    print("done")