import sys
import subprocess
from pathlib import Path


def run_command(*args):
    command = subprocess.run(args,
                             capture_output=True,
                             text=True)
    assert command.returncode == 0, command.stderr

    print(command.stdout)


def pprint_command(command):
    RESET = '\033[0m'
    GREEN = '\033[96m'
    print(f'{GREEN}{command}{RESET}')


def test_env():
    assert str(Path('../').resolve()) in set(sys.path)


def test_csv2plaintext():
    pprint_command('$ csv2plaintext test.csv clr')
    run_command('../scripts/csv2plaintext', 'test.csv', 'clr')


def test_csv2markdown():
    pprint_command('$ csv2markdown test.csv clr')
    run_command('../scripts/csv2markdown', 'test.csv', 'clr')
    pprint_command('$ csv2markdown test.csv --pretty')
    run_command('../scripts/csv2markdown', 'test.csv', '--pretty')
    pprint_command('$ csv2markdown test.csv ccc --pretty')
    run_command('../scripts/csv2markdown', 'test.csv', 'ccc', '--pretty')


def test_csv2latex():
    pprint_command('$ csv2latex test.csv clr')
    run_command('../scripts/csv2latex', 'test.csv', 'clr')
    pprint_command('$ csv2latex test.csv --pretty')
    run_command('../scripts/csv2latex', 'test.csv', '--pretty')
    pprint_command('$ csv2latex test.csv ccc --pretty')
    run_command('../scripts/csv2latex', 'test.csv', 'ccc', '--pretty')
