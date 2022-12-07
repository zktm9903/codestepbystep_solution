def print_entire_file():
    file_name = input('Type a file name: ')
    f = open(file_name, 'r')
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    f.close()
