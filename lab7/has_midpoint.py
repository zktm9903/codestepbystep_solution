def has_midpoint(a, b, c):
    abc = a + b + c
    
    mid = abc / 3
    
    if mid == a:
        return True
    if mid == b:
        return True
    if mid == c:
        return True
    
    return False