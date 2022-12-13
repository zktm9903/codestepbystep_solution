def repeat(strList, k):
#    result = []
#    for str in strList:
#        for i in range(k):
#            result.append(str)
#            
#    strList = result
#    return result

    copyStrList = []
    
    for str in strList:
        copyStrList.append(str)
        
    strList.clear()
    
    for str in copyStrList:
        for i in range(k):
            strList.append(str)
            
    return strList