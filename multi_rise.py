

import nbformat
from nbformat import NotebookNode, validate, from_dict
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from copy import deepcopy
from pprint import pprint
import os
import argparse
from pathlib import Path


def combine_nbs(nb_files=None, output=None):

    if "ipynb" not in output.suffix:
        output = output.with_suffix(".ipynb")

    if nb_files is None:
        nb_files = ['./Untitled.ipynb',
                    './Untitled2.ipynb',
                    './Untitled3.ipynb']

    combined_nb = new_notebook()

    for file in nb_files:
        nb = nbformat.read(file, as_version=4)
        combined_nb.metadata.merge(nb.metadata)
        nb.cells.append(
                new_code_cell("%reset -f",
                              metadata={
                                      "slideshow": {
                                          "slide_type": 'slide'
                                      }
                              }))
        nb.cells.append(
                new_markdown_cell("Execute for next speaker",
                                  metadata={
                                      "slideshow": {
                                          "slide_type": 'slide'
                                      }
                                  }))
        for cell in nb.cells:
            cell.metadata.origin = file
            combined_nb.cells.append(cell)

    nbformat.write(combined_nb, str(output))

def parse_index(fp):
    if is_instance(fp, Path):
        with fp.open() as f:
            nb_files = [fname for fname in f.readlines() if Path(fname).is_file()]
    return nb_files

def main(argv=None):
    ap = argparse.ArgumentParser(description='Convert a set of notebooks to HTML')
    ap.add_argument('--index', nargs='?', type=Path, default= 'index.txt')
    ap.add_argument('--output', nargs='?', type=Path, default='combined_nb.ipynb')
    args = ap.parse_args(argv)

    combine_nbs(nb_files=None, output=args.output)



if __name__ == '__main__':
    main()
