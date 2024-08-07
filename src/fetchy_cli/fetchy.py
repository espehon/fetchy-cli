# Copyright (c) 2024, espehon
# License: https://www.gnu.org/licenses/gpl-3.0.html


import os
import sys
import argparse
import json
import copy
import importlib.metadata


try:
    __version__ = f"fetchy {importlib.metadata.version('fetchy_cli')} from fetchy_cli"
except importlib.metadata.PackageNotFoundError:
    __version__ = "Package not installed..."

# Set file paths
storage_folder = os.path.expanduser("~/.share/fetchy/")
storage_file = "fetchy.json"
storage_path = storage_folder + storage_file


# Check if storage folder exists, create it if missing.
if os.path.exists(os.path.expanduser(storage_folder)) == False:
    os.makedirs(storage_folder)

# Check if storage file exists, create it if missing.
if os.path.exists(storage_path) == False:
    with open(storage_path, 'w', encoding='utf-8') as file:
        json.dump({}, file)

# read storage file
with open(storage_path, 'r') as file:
    data = json.load(file)


# Set argument parsing
parser = argparse.ArgumentParser(
    description="Fetchy: Fetch strings from your system rather than your own memory!",
    epilog="Homepage: https://github.com/espehon/fetchy-cli",
    allow_abbrev=False,
    add_help=False,
    usage="\n> fet -n pi 3.14159265359\n> fet pi\n3.14159265359",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('-?', '--help', action='help', help='Show this help message and exit.')
parser.add_argument('-v', '--version', action='version', version=__version__, help="Show package version and exit.")
parser.add_argument('-c', '--copy', nargs=1, metavar='N', action='store', type=str, help='Copy the value of [N] to the clipboard.')
parser.add_argument('-l', '--list', action='store_true', help='List saved variable names.')
parser.add_argument('-n', '--new', nargs=2, type=str, metavar=('N', 'V'), help='Create [N] with the value of [V]. (Overwrite existing)')
parser.add_argument('-d', '--delete', nargs='+', metavar=('N1', 'N2'), action='store', type=str, help='Delete [N1] etc.')
parser.add_argument('-r', '--rename', nargs=2, type=str, metavar=('O', 'N'), help='Rename [O] to [N].')





def read_storage():
    pass


def cli(argv=None):
    args = parser.parse_args(argv) #Execute parse_args()
    pass