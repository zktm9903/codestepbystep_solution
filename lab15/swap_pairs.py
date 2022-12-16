def swap_pairs(strList):
    for i in range(1, len(strList), 2):
        tmp = strList[i-1]
        strList[i-1] = strList[i]
        strList[i] = tmp
    return strList