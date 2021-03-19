📦 CSV converter
======================

This is a Python utility for converting a .csv file to other readable table formats.

**DEMO:**
![demo-gif](https://user-images.githubusercontent.com/50312506/108581092-8b413980-7369-11eb-932e-3b458212176a.gif)



## Usage

Supported options:

- `alignment`: a string consisting of alignment specifiers in `('c', 'l', 'r')`, has the same length of table columns.
    Literally, `c` is shorten for `center-aligned`, and similarly `l` is for `left-aligned`, `r` is for `right-aligned`, thereby, `clr` denotes that a 3-column table with center-aligned, left-aligned, and right-aligned alignment in each column.
    By default, the first column of the table is center-aligned, and the other columns is left-aligned, i.e. for a 3-column table, `alignment=cll`;
- `pretty`: bool value, means whether to format the stdout with a better visualization.

### Shell Command

Before doing anything else, make sure that `./scripts` directory has been added to the System `$Path`:

```bash
$ source shell-commands.sh
```

Then,

- `csv2plaintext`

    ```bash
    $ csv2plaintext sample.csv [clr]
    ```

- `csv2markdown`

    ```bash
    $ csv2markdown sample.csv [clr] [--pretty]
    ```

- `csv2latex`

    ```
    $ csv2latex sample.csv [clr] [--pretty]
    ```

### Package

You should put this package in the same directory as your working scripts, otherwise you
should first add the directory of this package to the `$PYTHONPATH`:

```bash
$ export PYTHONPATH=$PWD
```

then imports them as you want:

- `csv2plaintext`

    - .csv file:

    ```python
    >>> from csv_converter import csv2plaintext
    >>> output = csv2plaintext('sample.csv'[, alignment='clr'])
    ```

    - raw data variable (also supports csv-like string input):

    ```python
    >>> rawdata = """header1,header2,header3
    ... hi,this is a,csv file
    ... center-aligned column,left-aligned column,right-aligned column
    ... you can,check out the result,from stdout or necessary rendering
    ... """
    >>> output = csv2plaintext(rawdata[, alignment='clr'])
    ```

- `csv2markdown`

    ```python
    >>> from csv_converter import csv2markdown
    >>> output = csv2markdown('sample.csv'[, alignment='clr', pretty=True])
    ```

- `csv2latex`

    ```python
    >>> from csv_converter import csv2latex
    >>> output = csv2latex('sample.csv'[, alignment='clr', pretty=True])
    ```



## TODO

- [ ] `csv2markdown & csv2latex`: highlights concerned statistical descriptors, such as maximum/minimum values
