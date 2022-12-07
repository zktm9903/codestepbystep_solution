howMany = int(input('How many numbers? '))

count = 0
numArr = []
while(count < howMany):
    numArr.append(int(input('Next number? ')))
    count += 1

print('Biggest =', max(numArr))
print('Smallest =', min(numArr))