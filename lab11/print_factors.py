def print_factors(num):
    now = 1
    resultArr = []
    while 1:
        if num % now == 0:
            resultArr.append(str(now))
        if now == num:
            break
        now += 1
        
    print(' and '.join(resultArr))