from calendar import weekday
date =(input('Введите дату: ').split('.'))
year = int(date[2])
month = int(date[1])
day = int(date[0])
wd = weekday(year, month, day)
if wd == 0:
    print('Понедельник')
if wd == 1:
    print('Вторник')
if wd == 2:
    print('Среда')
if wd == 3:
    print('Четверг')
if wd == 4:
    print('Пятница')
if wd == 5:
    print('Суббота')
if wd == 6:
    print('Воскресенье')