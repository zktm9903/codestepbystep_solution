def even_sum_max():
    k = int(input('how many integers? '))
    max = 0
    sum = 0
    for i in range(k):
        n = int(input('next integer? '))
        if n % 2 == 0:
            sum += n
            if max < n:
                max = n
    print('even sum =', sum)
    print('even max =', max)