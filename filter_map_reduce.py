from random import randrange
from functools import reduce
n = int(input('Введите N: '))
num = [randrange(1,10) for i in range(n)]
print(num)
reducer, mapper, predicate = input('Введите условия: ').split(' ')
filters = {
    'adds': lambda x: x%2 != 0,
    'evens': lambda x: x%2 == 0,
    'simple': lambda x: x%2 != 0,
}
mappers = {
    'negate': lambda x: -x,
    'inverted': lambda x: 1/x,
    'squared': lambda x: x*x
}
reducers = {
    'sum': lambda x,y: x+y,
    'multipli': lambda x,y: x*y,
    'join': lambda x,y: int(str(x)+str(y)),
    'union': set(num),
    'reverse': lambda x: x[::-1]
}
first_num = {
    'sum': 0,
    'multipli': 1,
    'join': '',
    'union': [],
    'reverse': []
}
print([reduce(reducers[reducer], (*map(mappers[mapper], num), (*filter (filters[predicate], num))), first_num[reducer])])
