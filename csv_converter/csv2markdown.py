from .csv_converter import CsvConverter


def csv2markdown(*args, **kwargs):
    return CsvToMarkdown(*args, **kwargs).run()


class CsvToMarkdown(CsvConverter):

    @property
    def dest_type(self):
        return 'markdown'

    def run(self):
        code = ['\n'.join(
            (self.generate_each_row(self.header,
                                    separator='|',
                                    is_header=True),
             self._generate_format_line())
        )]
        code.append('\n'.join(
            (self.generate_each_row(row,
                                    separator='|')
             for row in self.body)
        ))

        return '\n'.join(code)

    @property
    def escape_chars(self):
        return ('|',)

    def _generate_format_line(self):
        if self.pretty:
            formats = [self._get_header_underline(input_specifier, width)
                       for input_specifier, width
                       in zip(self.alignment, self.max_width_each_col)]
        else:
            formats = [self._get_header_underline(input_specifier)
                       for input_specifier in self.alignment]

        return self.generate_each_row(formats,
                                      separator='|',
                                      is_split_line=True)

    @staticmethod
    def _get_header_underline(input_specifier, width=None):
        # width [+ int] is for consisting padding space on both side of cell
        # text in count
        if input_specifier == 'c':
            return ':{}:'.format('-' * width) if width is not None else ':---:'
        if input_specifier == 'l':
            return '-' * (width + 2) if width is not None else '---'
        if input_specifier == 'r':
            return '{}:'.format('-' * (width + 1)) if width is not None else '---:'
