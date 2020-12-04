import sys

flag, delemeter, file = sys.argv[1:]

with open(file, 'r') as file_obj:
    file_content = file_obj.readlines()
    file_content = [line.rstrip() for line in file_content]

if delemeter[1] == '-':
    start = int(delemeter[0]) - 1
    end = int(delemeter[2]) 

    for line in file_content:
        print(line[start:end])
elif delemeter[1] == ',':
    start = int(delemeter[0]) - 1
    stop = int(delemeter[2]) - 1

    for line in file_content:
        print(line[start], line[stop], end='')
        print(end="\n")

