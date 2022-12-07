def main():
    stick(SIZE)
    top(SIZE)
    mid(SIZE)
    bottom(SIZE)
    stick(SIZE)
    boldStick(SIZE)
    top(SIZE)
    mid(SIZE)

def stick(index):
    for k in range(0,index):
        for i in range(0,index):
            print('   ', end='')
        print('||')
    
def top(index):
    for k in range(0, index):
        for i in range(0, index-1-k):
            print('   ', end='')
        print('__/', end='')
        for i in range(0, k):
            print(':::', end='')
        print('||', end='')
        for i in range(0, k):
            print(':::', end='')
        print('\\__')
        
def mid(index):
    print('|', end='')
    for i in range(0, index):
        print('""""""', end='')
    print('|')
        
def bottom(index):
    for k in range(0, index):
        for i in range(0, k):
            print('  ', end='')
        print('\\_', end='')
        for i in range(0, index*3-1-2*k):
            print('/\\', end='')
        print('_/')
        
def boldStick(index):
    for k in range(0, index**2):
        for i in range(0, index*2+1):
            print(' ', end='')
        print('|', end='')
        for i in range(0, index-2):
            print('%', end='')
        print('||', end='')
        for i in range(0, index-2):
            print('%', end='')
        print('|')
        

main()