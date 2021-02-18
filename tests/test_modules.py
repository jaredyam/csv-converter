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
    output = csv2markdown('test.csv', pretty=False)
    print(output)
    output = csv2markdown('test.csv', alignment='ccc', pretty=False)
    print(output)


def test_csv2latex():
    output = csv2latex('test.csv')
    print(output)
    output = csv2latex('test.csv', alignment='clr')
    print(output)
    output = csv2latex('test.csv', pretty=False)
    print(output)
    output = csv2latex('test.csv', alignment='ccc', pretty=False)
    print(output)


def test_csv2plaintext_with_variable_input():
    rawdata = """header1,header2,header3
hi,this is a,csv file
center-aligned column,left-aligned column,right-aligned column
you can,check out the result,from stdout or necessary rendering
"""
    output = csv2plaintext(rawdata)
    print(output)
    output = csv2plaintext(rawdata, alignment='clr')
    print(output)
