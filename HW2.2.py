#Пользователь вводит N (N > 2), а затем список из N чисел. Найдите два наибольших числа в этом списке
n = int(input('Введите N: '))
i = 0
s = []
if n > 2:
    for item in range(n):
        s_add = input('Введите число: ')
        s.append(float(s_add))
    else:
        s = iter(s)
        max1 = next(s)
        max2 = None
    for item in s:
        if item > max1:
            max2 = max1
            max1 = item
        else:
            if max2 == None or max2 < item:
                max2 = item
    print ('Первое наибольшее число', max1, 'Второе наибольшее число', max2)
else:
    print('Введено неверное N')
