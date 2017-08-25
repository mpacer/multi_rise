# -*- coding: utf-8 -*-
import nbformat

from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


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
        if 'no_reset' not in nb.cells[-1].metadata.get("tags", []):
            nb.cells.append(
                    new_markdown_cell("Execute for next speaker",
                                      metadata={
                                          "slideshow": {
                                              "slide_type": 'slide'
                                          }
                                      }))
            nb.cells.append(
                    new_code_cell("%reset -f",
                                  metadata={
                                          "slideshow": {
                                              "slide_type": '-'
                                          }
                                  }))
        for cell in nb.cells:
            cell.metadata.origin = file
            combined_nb.cells.append(cell)

    combined_nb.metadata.pop("celltoolbar")
    nbformat.write(combined_nb, str(output))


if __name__ == '__main__':
    from . import main
    main()
