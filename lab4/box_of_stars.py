def box_of_stars(x, y):
    for i in range(0, x):
        print('*', end='')
    print()
    
    for i in range(0, y-2):
        print('*', end='')
        for i in range(0, x-2):
            print(' ', end='')
        print('*')
        
    for i in range(0, x):
        print('*', end='')