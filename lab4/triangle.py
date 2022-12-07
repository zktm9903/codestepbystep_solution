def triangle(idx):
    for k in range(0, idx):
        for i in range(0, idx-1-k):
            print(' ', end='')
        for i in range(0, k+1):
            print('*', end='')
        print()