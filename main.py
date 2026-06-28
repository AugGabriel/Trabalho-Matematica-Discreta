import os
from datetime import datetime

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


# preorder(simulation)