message = input('Your message? ').upper()
key = int(input('Encoding key? '))

messageArr = message.split()

for word in messageArr:
    for i in range(len(word)):
        if ord(word[i]) < 65 or ord(word[i]) > 122 or (ord(word[i]) > 90 and ord(word[i]) < 97):
            print(chr(ord(word[i])), end='')
            continue
        changeChar = ord(word[i])+key
        if changeChar > 90:
            print(chr(changeChar-90+64), end='')
        elif changeChar < 65:
            print(chr(91+(changeChar-65)), end='')
        else:
            print(chr(changeChar), end='')
    print(' ', end='')