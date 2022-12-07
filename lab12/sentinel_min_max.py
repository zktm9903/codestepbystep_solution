numArr = []

while 1:
    num = int(input('Type a number (or -1 to stop): '))
    if num == -1:
        break
    numArr.append(num)

if len(numArr) != 0:
    print('Maximum was', max(numArr))
    print('Minimum was', min(numArr))