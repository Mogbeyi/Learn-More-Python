import argparse

parser = argparse.ArgumentParser(description='Print out content of files')
parser.add_argument('files', metavar='F', type=str, nargs='+', 
                    help='A program to print content of files')

args = parser.parse_args()

for file in args.files:
    with open(file) as open_file:
        print(open_file.read())

