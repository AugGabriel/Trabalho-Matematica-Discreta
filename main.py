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
"""Image extensions accepted by the system"""


def depth_first_search(directory: DirEntry) -> Generator[DirEntry]:
    """
    Searches for all files inside the input dir.

    It iterates through all entries inside the directory; 
    if entry is a file, the function yields it; 
    else if it is a directory, it recursively, depth-first searches for all images inside.
    """

    for entry in directory:
        if not os.path.isdir(entry):
            # Entry is a file
            yield entry
        else:
            # Entry is a directory
            yield from depth_first_search(os.scandir(os.path.abspath(entry)))


def is_image(file: DirEntry):
    """
    Checks if file extension is in image extensions, 
    ultimately returning if file is an image accepted by the system
    """
    return file.name.split('.')[-1] in IMAGE_EXTENSIONS


def create_date_path(date: datetime, output: str) -> str:
    """
    Creates the path to that date in the format year/month/, 
    if it still does not exist
    """

    # Makes sure the output dir exists
    if not os.path.exists(output):
        os.mkdir(output)

    # Creates the year dir
    year_path = os.path.join(output, f"{date.year:4d}\\")
    if not os.path.exists(year_path):
        os.mkdir(year_path)

    # Creates the month dir
    month_path = os.path.join(year_path, f"{date.month:02d}\\")
    if not os.path.exists(month_path):
        os.mkdir(month_path)

    # Returns the path
    return month_path


def create_file_path(file: DirEntry, output: str):
    """
    Creates path to the file from its creation date.
    The output will be the prefix of the path
    """
    return create_date_path(datetime.fromtimestamp(os.path.getctime(file)), output)


def sort(input: str, output: str):
    """
    Sorts all images from the input directory 
    to the output directory, grouping by year, and then by month
    """

    # Gets all the files in the input directory
    files = depth_first_search(os.scandir(input))

    # Filters the files, keeping only the images
    images = [file for file in files if is_image(file)]

    for file in images:
        # Makes sure the correct path exists for file, and gets the path
        dst = create_file_path(file, output)

        # Copies the file from the input dir to the output dir, sorted and with its metadata
        shutil.copy2(file.path, dst)


def main():
    """Connects the tools to their use"""
    sort(INPUTDIR, OUTPUTDIR)


if __name__ == "__main__":
    sort()