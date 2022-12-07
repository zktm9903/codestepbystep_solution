def is_palindrome(word):
    word = word.upper()
    i = 0
    while(i < len(word)/2):
        for i in range(len(word)):
            if word[i] != word[len(word)-i-1]:
                return False
        i += 1
    return True