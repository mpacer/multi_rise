"""This is a quick shortcut to combine Jupyter notebooks into a single rise
presentation.  It adds a cell in between each notebook to reset the environment
so that the notebooks don't cause issues for each other."""

import argparse
from pathlib import Path

from .combine import combine_nbs

__version__ = '0.1.2'


def parse_index(fp):
    if isinstance(fp, Path):
        with fp.open() as f:
            nb_files = [fname.rstrip() for fname in f.readlines()
                        if Path(fname.rstrip()).is_file()]
    return nb_files


def main(argv=None):
    ap = argparse.ArgumentParser(description='Combine notebooks and make slides')
    ap.add_argument('--index', nargs='?', type=Path,
                    default='index.txt')
    ap.add_argument('--output', nargs='?', type=Path,
                    default='combined_nb.ipynb')
    args = ap.parse_args(argv)

    combine_nbs(nb_files=parse_index(args.index), output=args.output)
