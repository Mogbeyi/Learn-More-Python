import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='finds specific content files')
parser.add_argument('word', metavar='F', type=str, 
                    help='A program to print content of files')

parser.add_argument('files', metavar='F', type=str, nargs='+', 
                    help='A program to print content of files')

args = parser.parse_args()

def grep(args):
    def strip_new_line(word):
        return word.rstrip()

    def check_if_word_exist(word):
        return args.word in word 

    with open(args.files[0], 'r') as file_obj:
        content = [strip_new_line(content) for content in file_obj.readlines()]
        filter_object = [filtered_object for filtered_object in content if check_if_word_exist(filtered_object)]

    for word in filter_object:
        # Add color to specific word
        print(f'{word}'.replace(args.word, bcolors.FAIL + args.word + bcolors.ENDC))

grep(args)
