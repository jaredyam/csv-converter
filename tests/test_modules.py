from csv_converter import csv2plaintext
from csv_converter import csv2markdown
from csv_converter import csv2latex


def test_csv2plaintext():
    output = csv2plaintext('test.csv')
    print(output)
    output = csv2plaintext('test.csv', alignment='clr')
    print(output)


def test_csv2markdown():
    output = csv2markdown('test.csv')
    print(output)
    output = csv2markdown('test.csv', alignment='clr')
    print(output)
    output = csv2markdown('test.csv', pretty=True)
    print(output)
    output = csv2markdown('test.csv', alignment='ccc', pretty=True)
    print(output)


def test_csv2latex():
    output = csv2latex('test.csv')
    print(output)
    output = csv2latex('test.csv', alignment='clr')
    print(output)
    output = csv2latex('test.csv', pretty=True)
    print(output)
    output = csv2latex('test.csv', alignment='ccc', pretty=True)
    print(output)
