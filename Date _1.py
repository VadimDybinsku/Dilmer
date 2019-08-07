from calendar import weekday, day_name
from _datetime import datetime
now = datetime.now()
year, month = now.year, now.month
days = {key:value for value,key in enumerate(day_name)}
print(days)
day = input('Введите день недели: ')
for key, value in days.items():
    if key == day:
        day = value
while True:
    if weekday(year, month, 1) == day:
        break
    month = month + 1
    if month == 13:
        month = 1
        year = year + 1
print('Год: ', year, 'Месяц: ',month)
