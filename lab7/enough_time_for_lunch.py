def convertTime(hour, minute):
    return hour*60 + minute

def enough_time_for_lunch(h1, m1, h2, m2):
    start = convertTime(h1, m1)
    end = convertTime(h2, m2)
    dif = end - start
   
    if dif >= 45: return True
    
    return False