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
    path = Path(directory)
    for p in path.rglob('*.py'):
        load_module(p.as_posix(), p.stem)


def load_bundled():
    directory = PurePath(Path(__file__).parent, 'extensions')
    load_directory(directory)
