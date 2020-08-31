"""
    initialize directory to hold ADR files.
    create directories as needed, but exsting directory may be used
"""

import pathlib
import new_adr
import util


def create_adr_dir(adr_dir_name):
    adr_path = pathlib.PosixPath(adr_dir_name)
    adr_path.mkdir(exist_ok=True, parents=True)
    return adr_path


def write_adr_dir_file(adr_dir_file_name, adr_path):
    with open(adr_dir_file_name, "w") as adir_dir_file:
        adir_dir_file.write(str(adr_path))


def init_adr_dir(adr_dir_name, adr_dir_file_name):
    adr_path = create_adr_dir(adr_dir_name)
    write_adr_dir_file(adr_dir_file_name, adr_path)
    util.write_adr(*new_adr.first_adr(adr_path))
