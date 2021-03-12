from .csv_converter import CsvConverter


def csv2latex(*args, ** kwargs):
    return CsvToLatex(*args, ** kwargs).run()


class CsvToLatex(CsvConverter):

    @property
    def dest_type(self):
        return 'latex'

    def run(self):
        code = ['\n'.join(
            ('\\begin{table}',
             '\\centering\n\\resizebox{\\textwidth}{!}{%',
             '\\begin{{tabular}}{{{}}}'.format(self.alignment),
             '\\toprule')
        )]
        code.append(self.generate_each_row(self.header,
                                           separator='&',
                                           is_header=True,
                                           with_border=False)
                    + ' \\\\')
        code.append('\\midrule')
        code.append('\n'.join(
            (self.generate_each_row(row,
                                    separator='&',
                                    with_border=False)
             + ' \\\\')
            for row in self.body))
        code.append('\n'.join(
            ('\\bottomrule',
             '\\end{tabular}',
             '}',
             '\\end{table}')
        ))

        return '\n'.join(code)

    @property
    def escape_chars(self):
        return ('&', '%',)
