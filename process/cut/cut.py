import sys

flag, delemeter, file = sys.argv[1:]

def cut(flag, delemeter, file):
    with open(file, 'r') as file_obj:
        file_content = file_obj.readlines()
        file_content = [line.rstrip() for line in file_content]

    if delemeter[1] == '-':
        print_hyphen_separator(delemeter, file_content)
    elif delemeter[1] == ',':
        print_comma_separator(delemeter, file_content)

def print_hyphen_separator(delemeter, file_content):
    start = int(delemeter[0]) - 1
    end = int(delemeter[2]) 

    for line in file_content:
        print(line[start: end])
 
def print_comma_separator(delemeter, file_content):
    start = int(delemeter[0]) - 1
    stop = int(delemeter[2]) - 1

    for line in file_content:
        print(line[start], line[stop])

cut(flag, delemeter, file)
