# numpydoctor

Tools for completion, correction, and checking of numpydoc-style
docstrings in Python.

### Setup

Clone this repo and `pip install .`

### Usage

```console
$ numpydoctor -h
usage: numpydoctor [-h] [-o OFFSET] [-N] [-p] [-m] [-a] {check,fix} ... path

Numpydoc-style docstring checking & completion

positional arguments:
  {check,fix}           action subcommands
    check               check docstring information.
    fix                 fix docstring information.
  path                  path to python module source file

optional arguments:
  -h, --help            show this help message and exit
  -o OFFSET, --offset OFFSET
                        cursor byte offset in `file` of scope to check,
                        optional. If omitted, will check all docstrings.
  -N, --nested          include functions & classes nested in other functions
  -p, --private         include private names
  -m, --magic           include magic names
  -a, --all             include all names (equivalent to -pm)

$ numpydoctor check -h
usage: numpydoctor check [-h] [-M]

Check docstring information. Find module, class, function, and coroutine
definitions in source code whose docstrings contain incorrect or outdated
information, or are missing docstrings entirely.

optional arguments:
  -h, --help     show this help message and exit
  -M, --missing  only check for missing docstrings

$ numpydoctor fix -h
usage: numpydoctor fix [-h] [-M] [-i] [-L LINE_WRAP_COL] [-I INDENT_SIZE] [-T]

Fix docstring information. Gather information about modules, functions,
classes, and coroutines through static analysis and modify docstrings,
inserting missing information and correcting out-of-date documentation.

optional arguments:
  -h, --help            show this help message and exit
  -M, --missing         only add missing docstrings, do not fix existing
                        docstrings
  -i, --inplace         modify the file in-place (default: write to stdout)
  -L LINE_WRAP_COL, --line-wrap-col LINE_WRAP_COL
                        line wrap column for docstrings (default: None)
  -I INDENT_SIZE, --indent-size INDENT_SIZE
                        size of indentation in spaces (default: 4)
  -T, --todo            control where TODO messages are inserted for missing
                        docstring data. Repeating this argument will make it
                        more pedantic. By default, TODO messages will be
                        inserted where required data is missing -- parameter
                        names, return types. Each additional level will insert
                        TODOs for missing types, descriptions, return names,
                        and extended summaries.
```
