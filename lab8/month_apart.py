def convertDays(m, d):
    return m*30 + d

def month_apart(m1, d1, m2, d2):
    days1 = convertDays(m1, d1)
    days2 = convertDays(m2, d2)
    
    differDays = abs(days1 - days2)
    
    if differDays >= 30:
        return True
    
    return False