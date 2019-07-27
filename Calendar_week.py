from calendar import weekday
date =input('Введите дату: ')
day, month, year = map(int,date.split('.'))
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