def print_num_range(a, b):
    numArr = []
    differ = 0
    if a < b:
        differ = 1
    else:
        differ = -1
    while 1:
        numArr.append(a)
        
        if a==b:
            break
            
        a += differ
    print(numArr)