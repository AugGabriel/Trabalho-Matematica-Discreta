import os
from pathlib import Path
import shutil
from datetime import datetime
from collections.abc import Iterator

ROOTDIR = Path(__file__).resolve().parent
INPUTDIR = ROOTDIR / "input"
OUTPUTDIR = ROOTDIR / "output"

IMAGE_EXTENSIONS = [
    ".png", 
    ".jpg", 
    ".jpeg", 
    ".webp", 
    ".avif",
]
"""Image extensions accepted by the system"""

GROUP_BY_DAY = False
"""
Determines whether images should be grouped by day inside each month directory
"""


def depth_first_search(directory: Path) -> Iterator[Path]:
    """
    Searches recursively for all files inside the given directory.

    It iterates through all entries inside the directory; 
    if an entry is a file, it is yielded; 
    Otherwise, if it is a directory, the function recursively performs a depth-first search for files inside it.
    """

    for entry in directory.iterdir():
        if entry.is_file():
            # Entry is a file
            yield entry
        else:
            # Entry is a directory
            yield from depth_first_search(entry)


def is_image(file: Path):
    """
    Returns whether the file has an image extension supported by the system
    """
    return file.suffix.lower() in IMAGE_EXTENSIONS


def create_date_path(date: datetime, output: Path) -> Path:
    """
    Creates the directory structure for the given date in the format year/month/, and optionally day/, 
    if it still does not exist
    """
    
    # Makes sure the output directory exists
    output.mkdir(exist_ok=True)
    
    # Builds the path to the month directory
    month_path = output / f"{date.year:4d}" / f"{date.month:02d}"

    # Gets the path for the day directory
    if GROUP_BY_DAY:
        day_path = month_path / f"{date.day:02d}"

        # Creates the path for the day directory
        day_path.mkdir(parents=True, exist_ok=True)

        # Returns the path, grouping by day
        return day_path

    # Creates the path for the month directory
    month_path.mkdir(parents=True, exist_ok=True)

    # Returns the path, not grouping by day
    return month_path


def create_file_path(file: Path, output: Path):
    """
    Creates the destination path to the file based on it's creation date.
    The output will be the prefix of the path
    """
    return create_date_path(datetime.fromtimestamp(os.path.getctime(file)), output)


def sort(input: Path, output: Path):
    """
    Organizes all images from the input directory 
    to the output directory, grouping by year, and then by month
    """

    # Iterates through every file in the input directory
    for file in depth_first_search(input):

        # Filters the files, keeping only the images
        if not is_image(file):
            continue

        # Makes sure the correct path exists for file, and gets the path
        dst = create_file_path(file, output)

        # Copies the file from the input directory to the output directory, sorted and with its metadata
        shutil.copy2(file, dst)


def main():
    """Connects the tools to their use"""
    sort(INPUTDIR, OUTPUTDIR)


if __name__ == "__main__":
    main()