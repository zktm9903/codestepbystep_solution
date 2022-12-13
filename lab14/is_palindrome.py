def is_palindrome(strList):
    for i in range(len(strList)):
        if strList[i] != strList[len(strList)-i-1]:
            return False
    return True