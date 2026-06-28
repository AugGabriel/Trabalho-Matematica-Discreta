import os
from os import DirEntry
import shutil
from datetime import datetime
from collections.abc import Generator

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
INPUTDIR = os.path.join(ROOTDIR, "input\\")
OUTPUTDIR = os.path.join(ROOTDIR, "output\\")

IMAGE_EXTENSIONS = [
    "png", "jpg", "jpeg", "webp", "avif",
]


def is_image(file: DirEntry):
    """
    Checks if file extension is in image extensions, 
    ultimately returning if file is an image
    """
    return file.name.split('.')[-1] in IMAGE_EXTENSIONS


def create_dir(date: datetime) -> str:
    """Creates directory by date, if it still does not exist"""

    # Makes sure the output dir exists
    if not os.path.exists(OUTPUTDIR):
        os.mkdir(OUTPUTDIR)

    # Creates the year dir
    year_path = os.path.join(OUTPUTDIR, f"{date.year:4d}\\")
    if not os.path.exists(year_path):
        os.mkdir(year_path)

    # Creates the month dir
    month_path = os.path.join(year_path, f"{date.month:02d}\\")
    if not os.path.exists(month_path):
        os.mkdir(month_path)

    # Returns the path
    return month_path


def create_from_entry(entry: DirEntry):
    """Creates directory from file's creation date, using create_dir"""
    return create_dir(datetime.fromtimestamp(os.path.getctime(entry)))


def preorder(directory: DirEntry) -> Generator[DirEntry]:
    """Searches for all images inside the input dir"""

    for entry in directory:
        if not os.path.isdir(entry):
            # Entry is a file
            # date = datetime.fromtimestamp(os.path.getctime(entry)).strftime("%Y/%m")
            yield entry
        else:
            # Entry is a directory
            yield from preorder(os.scandir(os.path.abspath(entry)))


def sort():
    """
    Main function, responsible by sorting all images from input directory 
    to the output directory, grouping by year, and then by month
    """

    # Gets all the files in the input directory
    files = preorder(os.scandir(INPUTDIR))

    # Filters the files, keeping only the images
    images = [file for file in files if is_image(file)]

    for file in images:
        # Makes sure the correct path exists for file, and gets the path
        dst = create_from_entry(file)

        # Copies the file from the input dir to the output dir, sorted and with its metadata
        shutil.copy2(file.path, dst)


# simulation = [1, 2, 3, [4, 5, [6, 7, 8], 9, 10], 11, [12, 13]]
# simulation = os.scandir(INPUTDIR)

sort()