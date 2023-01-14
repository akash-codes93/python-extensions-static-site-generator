import sys
import importlib

from pathlib import Path, PurePath


def load_module(directory, name):

    # to add path to the sys
    sys.path.insert(0, directory)

    # to import module
    importlib.import_module(name)

    # removing the path
    sys.path.pop(0)


def load_directory(directory):
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)


def load_bundled():
    directory = Path(__file__).parent / "extensions"
    load_directory(directory)
