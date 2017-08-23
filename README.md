If you want to use this create an index.txt file with a sequence of paths to your files each on a new line in the order you wish them to be included in your final presentation.

Then use with this file in the directory.

```bash
multi_rise --index=index.txt --output=output.ipynb
```

where index is the index file and output is the name of the output file.

The index file is a file that contains file paths that will be combined into the final notebook. 

* The order in which the files appear in the index file is the order in which they'll be combined into the final notebook.
* Files can appear more than once.
* The file paths should be relative to the working directory in which the command is invoked.
* The file paths should only appear one per line
* It currently does no safe catching (e.g., of spaces) for you.


This only works on python 3.4+.
