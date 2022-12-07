def reverse(word):
    reverseWord = ''
    for i in range(len(word)-1, -1, -1):
        reverseWord += word[i]
        
    return reverseWord