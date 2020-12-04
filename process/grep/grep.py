
import argparse

parser = argparse.ArgumentParser(description='finds specific content files')
parser.add_argument('word', metavar='F', type=str, 
                    help='A program to print content of files')

parser.add_argument('files', metavar='F', type=str, nargs='+', 
                    help='A program to print content of files')

args = parser.parse_args()

def strip_new_line(word):
    return word.rstrip()

def check_if_word_exist(word):
    return args.word in word 

with open(args.files[0], 'r') as file_obj:
    content = [strip_new_line(content) for content in file_obj.readlines()]
    filter_object = [filtered_object for filtered_object in content if check_if_word_exist(filtered_object)]

for word in filter_object:
    print(word)
