📦 CSV converter
======================

This is a Python utility for converting a .csv file to other readable table formats.

**DEMO:**
![demo-gif](./imgs/demo.gif)


## Usage

Supported options:

- `alignment`: a string, which consists of alignment specifiers in ('c', 'l', 'r') and has the same length of table columns.
    Literally, `c` is shorten for `center-aligned`, `l` means `left-aligned`, `r` means `right-aligned`, thereby, `clr` means that the first column of the table is center-aligned, the second column is left-aligned, and the third column is right-aligned.
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

- `csv2plaintext`

    ```python
    >>> from csv_converter import csv2plaintext
    >>> output = csv2plaintext('sample.csv'[, alignment='clr'])
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
