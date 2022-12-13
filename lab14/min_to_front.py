def min_to_front(intList):
    minValue = min(intList)
    intList.remove(minValue)
    intList.insert(0,minValue) 
    return intList