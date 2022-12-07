def main():
    a = 7
    b = 42
    smaller = minimum(a, b)
    if smaller == a:
        print("a is the smallest!") 

def minimum(a, b):
    smaller = 0
    if a < b:
        smaller = a
    else: 
        smaller = b
    return smaller

main()