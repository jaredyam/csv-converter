import csv
import argparse


class CsvConverter():

    """Convert a .csv file to other readable formats.

    Attributes
    ----------
    csvfile : str
        Path to the .csv file.
        If the input is not a valid path/file, try to read as the raw data.
    alignment : str, default='c' + 'l' * (n_cols - 1)
        Group of alignment specifiers consisting of (`c`, `l`, `r`) has the
        same length as the table columns. `c` literally represents center-aligned
        format specifier, `l` represents left, `r` represents right. By default,
        the first column is center-aligned, and the other columns are left-aligned,
        i.e. `alignment='c' + 'l' * (n_cols - 1)`.
    pretty : bool, default=False
        Whether to format the output text/source code with a better visualization.
    """

    def __init__(self,
                 csvfile=None,
                 alignment=None,
                 pretty=True,
                 from_command_line=False):

        if from_command_line:
            args = self.parse_args()

            csvfile = args.csvfile
            alignment = args.alignment
            if not self.dest_type == 'plain text':
                pretty = args.pretty

        self.csvfile = csvfile
        self.header, self.body = self.get_header_and_body()

        if alignment is not None:
            assert set(alignment).issubset({'r', 'c', 'l'})
            assert len(alignment) == len(self.header), (
                'expected alignment format specifiers of length {}, got len({})={}'.format(
                    len(self.header), alignment, len(alignment)))
            self.alignment = alignment
        else:
            self.alignment = 'c' + 'l' * (len(self.header) - 1)

        self.pretty = pretty
        if self.pretty:
            self.max_width_each_col = self.get_max_width_each_col()
            self.format_dict = {'c': '^', 'l': '<', 'r': '>'}

    def run(self):
        raise NotImplementedError

    def dest_type(self):
        raise NotImplementedError

    @property
    def escape_chars(self):
        return ()

    def parse_args(self):
        parser = argparse.ArgumentParser(
            'Convert .csv file to {} table'.format(self.dest_type))

        parser.add_argument('csvfile', type=str, help='input .csv file')
        parser.add_argument('alignment', type=str, nargs='?',
                            help=('group of alignment specifiers consisting of (c, l, r) '
                                  'with the same length of table columns'))
        if not self.dest_type == 'plain text':
            # In the CLI mode, plain text has pretty visualization by default,
            # thus no need --pretty option
            parser.add_argument('--pretty', action='store_true',
                                help='better visualization of stdout')

        return parser.parse_args()

    def get_csv_generator(self):
        # conditions for recognising raw data input
        if len(self.csvfile.split('\n')) > 1 or len(self.csvfile.split(',')) > 1:
            rawdata = self.csvfile.splitlines()
        else:
            rawdata = open(self.csvfile, 'r')

        return ([i.strip() for i in row] for row in csv.reader(rawdata))

    def get_header_and_body(self):
        rows = self.get_csv_generator()
        header = next(rows)

        return header, rows

    def get_max_width_each_col(self):
        rows = self.get_csv_generator()
        max_width_each_col = [len(h) if h else 1 for h in next(rows)]
        for row in rows:
            for i, cell in enumerate(row):
                if len(cell) > max_width_each_col[i]:
                    max_width_each_col[i] = len(cell)

        return max_width_each_col

    def generate_each_row(self, row, separator,
                          is_header=False,
                          is_split_line=False,
                          with_border=True):
        if len(row) > len(self.header):
            raise IOError(('inconsistent number of record fields. '
                           'The line \'{}\' has {} fields, '
                           'while the header only has {} fields').format(
                ','.join(row), len(row), len(self.header)))

        row = [(cell.title() if is_header and cell.islower() else cell) if cell
               else '-' for cell in row]

        for c in self.escape_chars:
            row = [cell.replace(c, '\\' + c) for cell in row]

        if self.pretty and not is_split_line:
            # pad space on both side of cell text for better visualization
            row = [' {: {}{}} '.format(cell, self.format_dict[align_char], length)
                   for cell, align_char, length
                   in zip(row,
                          'c' * len(self.header) if is_header
                          else self.alignment,
                          self.max_width_each_col)]

        return '{}'.format(separator).join([''] + row + [''] if with_border else row)
