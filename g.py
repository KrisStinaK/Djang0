from random import randint


flag = True


def is_valid(a, n):
    if a.isdigit() and n >= int(a) >= 1:
        return True
    return False


def game():
    global flag
    print('Введите число')
    n = int(input())
    count = 0

    a = randint(1, n)
    print(a)
    print(f'Добро пожаловать в числовую угадайку\nВедите число от 1 до {n}')
    while True:
        digit = input()
        f = is_valid(digit, n)

        if f is False:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
        else:
            digit = int(digit)
            count += 1
            if a == digit:
                print('Вы угадали, поздравляем!')
                print(f'Количество попыток: {count}')
                print('Спасибо, что играли в числовую угадайку. Желаете сыграть еще раз?')
                s = input()
                if s.lower() == 'yes':
                    game()
                else:
                    print('До свидания!')
                    flag = False
                break
            elif a > digit:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif a < digit:
                print('Ваше число больше загаданного, попробуйте еще разок')


while flag:
    game()
