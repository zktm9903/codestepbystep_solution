import random

maximum = 100


def printExplanation():
    print('This program allows you to guess random numbers.')
    print('I will think of a number between 1 and 100')
    print('and you will try to guess it.')
    print('After each guess, I will give you a clue about')
    print('whether the correct number is higher or lower.')
    print()


def playing():
    result = []

    printExplanation()
    while 1:
        ans = random.randint(1, maximum)
        count = 0

        print('I\'m thinking of a number between 1 and 100...')
        while 1:
            num = int(input('Your guess? '))

            count += 1
            if num == ans:
                break
            elif num > ans:
                print('It\'s lower.')
            else:
                print('It\'s higher.')

        if count != 1:
            print(f'You got it right in {count} guesses!')
        else:
            print('You got it right in 1 guess!')
        result.append(count)

        restart = input('Do you want to play again? ')
        print()
        if restart[0].upper() != 'Y':
            break
    return result


def printResult(result):
    print('Overall results:')
    print('Total games   =', len(result))
    print('Total guesses =', sum(result))
    print('Guesses/game  =', round(sum(result) / len(result), 1))
    print('Best game     =', min(result))


def main():
    printResult(playing())


main()
