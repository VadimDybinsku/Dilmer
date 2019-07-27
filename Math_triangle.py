from math import acos, pi
a = int(input('Введите сторону A: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))
if a > 0 and b > 0 and c > 0:
    ange_a = acos((b**2 + c**2 - a**2)/(2*b*c)) * 180/pi
    ange_b = acos((a**2 + c**2 - b**2)/(2*a*c)) * 180/pi
    ange_c = acos((a**2 + b**2 - c**2)/(2*a*b)) * 180/pi
    print('Угол a = ', ange_a, 'Угол b = ', ange_b, 'Угол c = ', ange_c)
else:
    print('Введено неверное значение')