from random import randrange
nymber = randrange(1,11)
while True:
    x = int(input('Введите число: '))
    if x == nymber:
        print('Поздравляю! Вы угадали! Загаданное число: ', nymber)
    else:
        continue