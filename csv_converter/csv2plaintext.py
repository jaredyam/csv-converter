from .csv_converter import CsvConverter


__all__ = ['csv2plaintext']


def csv2plaintext(*args, **kwargs):
    return CsvToPlainText(*args, **kwargs).run()


class CsvToPlainText(CsvConverter):

    def __init__(self,
                 csvfile=None,
                 alignment=None,
                 from_command_line=False):
        super(CsvToPlainText, self).__init__(csvfile=csvfile,
                                             alignment=alignment,
                                             from_command_line=from_command_line)

    @property
    def dest_type(self):
        return 'plain text'

    def run(self):
        table_lines = ['\n'.join(
            (self._generate_split_line(),
             self.generate_each_row(self.header,
                                    separator='|',
                                    is_header=True),
             self._generate_split_line()
             )
        )]
        table_lines.append('\n'.join(
            (self.generate_each_row(row,
                                    separator='|')
             for row in self.body)
        ))
        table_lines.append(
            self._generate_split_line()
        )

        return '\n'.join(table_lines)

    def _generate_split_line(self):
        # width + 2 is for considering padding apace on both side of cell text
        # in count
        return self.generate_each_row(('-' * (width + 2)
                                       for width in self.max_width_each_col),
                                      separator='+',
                                      is_split_line=True)
