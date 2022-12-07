def add_commas(numStr):
    resultArr = []
    while 1:
        if len(numStr) > 3:
            resultArr.insert(0, numStr[-3:])
            numStr = numStr[:-3]
        else:
            resultArr.insert(0, numStr)
            break
    
    return ','.join(resultArr)