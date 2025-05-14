from random import randint

WELCOME_TEXT = 'Угадайте число от 1 до 100'
print(WELCOME_TEXT)
number = randint(0, 100)

def main():
    while True:
        guess = int(input('Введите число: '))

        if guess > number:
            print('Ваше число больше загаданного')
        if guess < number:
            print('Ваше число меньше загаданного')
        if guess == number:
            break
    print('Вы победили!')


main()