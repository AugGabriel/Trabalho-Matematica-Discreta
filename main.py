import os
from datetime import datetime
from win32_setctime import setctime

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
SIMPATH = os.path.join(ROOTDIR, "simulation/")


def preorder(directory):
    for entry in directory:
        if not os.path.isdir(entry):
            # Entry is a file
            date = datetime.fromtimestamp(os.path.getmtime(entry)).strftime("%Y/%m")
            print(str(entry) + "\t" + date)
        else:
            # Entry is a directory
            preorder(os.scandir(os.path.abspath(entry)))


# simulation = [1, 2, 3, [4, 5, [6, 7, 8], 9, 10], 11, [12, 13]]
simulation = os.scandir(SIMPATH)

def modify_date():
    PATH = os.path.join(SIMPATH, "downloads/15-12-2025.avif")
    DATE = datetime(2025, 12, 15).timestamp()
    os.utime(PATH, (DATE, DATE))
    setctime(PATH, DATE)

    print("done")

# preorder(simulation)
modify_date()