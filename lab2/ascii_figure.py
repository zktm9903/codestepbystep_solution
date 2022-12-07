def ascii_figure():
    index = 5
    for i in range(0, index):
        for j in range(0, index-i-1):
            print('////', end='')
        for j in range(0, i*2):
            print('****', end='')
        for j in range(0, index-i-1):
            print('\\\\\\\\', end='')
        print('')