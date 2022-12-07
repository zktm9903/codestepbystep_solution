def print_letters(text):
    for i in range(0, len(text)):
        if i == len(text)-1:
            print(text[i], end="")
        else:
            print(text[i] + "-", end="")
    print()   # to end the line of output