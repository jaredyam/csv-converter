import csv
import argparse
from pathlib import Path
from abc import ABC, abstractmethod, abstractproperty


class CsvConverter(ABC):

    """Convert a .csv file to other readable formats.

    Attributes
    ----------
    csvfile : str
        Path to .csv file.
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
                 pretty=False,
                 from_command_line=False):

        if from_command_line:
            args = self.parse_args(dest_type=self.dest_type, pretty=pretty)

            csvfile = args.csvfile
            alignment = args.alignment
            if pretty is False:
                # the --pretty command line option is only available
                # when the initial value is False
                pretty = args.pretty

        assert Path(csvfile).suffix == '.csv'
        self.csvfile = csvfile
        self.header, self.body = self.get_header_and_body()

        if alignment is not None:
            assert set(alignment).issubset({'r', 'c', 'l'})
            assert len(alignment) == len(self.header), (
                f'expected alignment format specifiers of length {len(self.header)}, '
                f'got len({alignment})={len(alignment)}')
            self.alignment = alignment
        else:
            self.alignment = 'c' + 'l' * (len(self.header) - 1)

        self.pretty = pretty
        if self.pretty:
            self.max_width_each_col = self.get_max_width_each_col()
            self.format_dict = {'c': '^', 'l': '<', 'r': '>'}

    @abstractmethod
    def run(self):
        pass

    @abstractproperty
    def dest_type(self):
        pass

    def parse_args(self, dest_type, pretty):
        parser = argparse.ArgumentParser(f'Convert .csv file to {dest_type} table')

        parser.add_argument('csvfile', type=str, help='input .csv file')
        parser.add_argument('alignment', type=str, nargs='?',
                            help=('group of alignment specifiers consisting of (c, l, r) '
                                  'with the same length of table columns'))
        if pretty is False:
            parser.add_argument('--pretty', action='store_true',
                                help='better visualization of stdout')

        args = parser.parse_args()

        return args

    def get_csv_generator(self):
        return csv.reader(open(self.csvfile, 'r'))

    def get_header_and_body(self):
        rows = self.get_csv_generator()
        header = next(rows)
        body = (row for row in rows)

        return header, body

    def get_max_width_each_col(self):
        rows = self.get_csv_generator()
        return [max(len(i) for i in col) for col in zip(*rows)]

    def generate_each_row(self, row, separator,
                          is_header=False,
                          is_split_line=False,
                          with_border=True):
        row = [(cell.title() if is_header else cell).strip() if cell
               else '-' for cell in row]

        if self.pretty and not is_split_line:
            # pad space on both side of cell text for better visualization
            row = [f' {cell: {self.format_dict[align_char]}{length}} '
                   for cell, align_char, length
                   in zip(row,
                          'c' * len(self.header) if is_header
                          else self.alignment,
                          self.max_width_each_col)]

        return f'{separator}'.join([''] + row + [''] if with_border else row)
