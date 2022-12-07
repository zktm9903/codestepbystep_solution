import random

point = 0

print('Welcome to Piglet!')

while 1:
    num = random.randrange(1,7)
    print('You rolled a', num)
    
    point += num
    
    if num == 1:
        point = 0
        break
    
    restart = input('Roll again? ')
    if restart == 'no':
        break;

print(f"You got {point} points.")
