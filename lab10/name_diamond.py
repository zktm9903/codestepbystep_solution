def name_diamond(word):
    for i in range(len(word)):
        print(word[:i+1])
    
    for i in range(len(word)):
        print(' '*(i+1), end='')
        print(word[i+1:])