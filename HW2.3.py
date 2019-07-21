#Пользователь вводит N, а затем список из N чисел. Если среди элементов есть нули, переместите их в начало списка
#(оставшиеся элементы должны остаться в исходном порядке), и выведите на экран получившийся список.
n = int(input('Введите N: '))
i = 0
s = []
answer = []
if n > 2:
    for item in range(n):
        s_add = input('Введите число: ')
        s.append(float(s_add))
    for item in s:
        if item == 0:
            answer.insert(0,item)
        if item != 0:
            answer.append(item)
print(answer)
