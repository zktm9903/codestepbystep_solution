def xo(k):
    for i in range(k):
        for j in range(k):
            if i==j or (k-1-i)==j:
                print('x', end='')
            else:
                print('o', end='')
            
        print()