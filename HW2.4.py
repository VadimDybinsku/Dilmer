#Пользователь вводит x и N. Посчитайте приблизительное значение cos(x) с точностью до N-ого члена его разложения: cos x = 1 - x**2/2!+x**4/4!-...
x = int(input('Введите X: '))
n = int(input('Введите N: '))
if n < 0:
    n = -n
power = 2
members = 0
def factorial(fact):
    if fact == 0:
        return 1
    else:
        return fact * factorial(fact - 1)
for i in range(n-1):
    members = members + x**power / factorial(power)
    power = power + 2
cos_x = 1 - members
print('cos x = ', cos_x)