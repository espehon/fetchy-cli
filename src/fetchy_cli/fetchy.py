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

# Set user paths
# home = os.path.expanduser("~") # not needed?
storage_path = os.path.expanduser("~/.share/tasky/")

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
parser.add_argument('-n', '--new', nargs=2, type=str, metavar=('N', 'V'), help='Assign [V] to [N].')
parser.add_argument('-d', '--delete', nargs='+', metavar=('N1', 'N2'), action='store', type=str, help='Delete [N1] etc.')





def cli(argv=None):
    args = parser.parse_args(argv) #Execute parse_args()
    pass