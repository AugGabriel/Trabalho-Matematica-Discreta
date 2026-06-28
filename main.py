import os
from pathlib import Path
import shutil
from datetime import datetime
from collections.abc import Iterator

ROOTDIR = Path(__file__).resolve().parent
INPUTDIR = ROOTDIR / "input"
OUTPUTDIR = ROOTDIR / "output"

IMAGE_EXTENSIONS = [
    "png", "jpg", "jpeg", "webp", "avif",
]
"""Image extensions accepted by the system"""


def depth_first_search(directory: Path) -> Iterator[Path]:
    """
    Searches for all files inside the input dir.

    It iterates through all entries inside the directory; 
    if entry is a file, the function yields it; 
    else if it is a directory, it recursively, depth-first searches for all images inside.
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
    Checks if file extension is in image extensions, 
    ultimately returning if file is an image accepted by the system
    """
    return file.name.split('.')[-1] in IMAGE_EXTENSIONS


def create_date_path(date: datetime, output: Path) -> Path:
    """
    Creates the path to that date in the format year/month/, 
    if it still does not exist
    """
    
    # Makes sure the output dir exists
    if not output.exists():
        os.mkdir(output)

    # Creates the year dir
    year_path = output / f"{date.year:4d}"
    if not year_path.exists():
        os.mkdir(year_path)

    # Creates the month dir
    month_path = year_path / f"{date.month:02d}"
    if not month_path.exists():
        os.mkdir(month_path)

    # Returns the path
    return month_path


def create_file_path(file: Path, output: str):
    """
    Creates path to the file from its creation date.
    The output will be the prefix of the path
    """
    return create_date_path(datetime.fromtimestamp(os.path.getctime(file)), output)


def sort(input: Path, output: Path):
    """
    Sorts all images from the input directory 
    to the output directory, grouping by year, and then by month
    """

    # Gets all the files in the input directory
    files = depth_first_search(input)

    # Filters the files, keeping only the images
    images = [file for file in files if is_image(file)]

    for file in images:
        # Makes sure the correct path exists for file, and gets the path
        dst = create_file_path(file, output)

        # Copies the file from the input dir to the output dir, sorted and with its metadata
        shutil.copy2(file, dst)


def main():
    """Connects the tools to their use"""
    sort(INPUTDIR, OUTPUTDIR)


if __name__ == "__main__":
    main()