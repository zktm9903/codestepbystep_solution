def print_pyramid():
    index = 6
    for i in range(1, index + 1):
        print(' ' * (index - (i - 1)), end='')
        print('*' * (2 * i - 1))