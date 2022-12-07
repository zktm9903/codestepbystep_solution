def contribution(count1, count2, sum, total):
    sum = 122456
    times = int(input("Is your money multiplied 1 or 2 times? "))
    donation = int(input("And how much are you contributing? "))
    
    sum = sum + times * donation + 1000
    
    total += donation
    
    if times == 1:
        count1 += 1
    if times == 2:
        count2 += 1
