def cheerleader(a, b):
    for i in range(a):
        GOcnt = 0;
        now = 0;
        print('   '*i, end='')
        while True:
            if now % 2 == 0:
                print('Go ', end='')
                now += 1
                GOcnt += 1
            else:
                print('Team ', end='')
                now += 1
            
            if GOcnt == b:
                break
        print()