import re

pattern = re.compile(r'[+\-]?\d+(\.\d+)?$')
#pattern.match() - поиск совпадений
#pattern.split() - разбитие по шаблону
#pattern.search() - поиск по шаблону
numbers = [
    '1',
    '-2',
    '+3.45',
    '10.257',
    'hello',
    'end',
    'a123',
    '123a'
]
for num in numbers:
    print(num, pattern.match(num))
    print(num, pattern.search(num))


