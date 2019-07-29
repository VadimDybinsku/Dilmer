from calendar import weekday, day_name
day, month, year = map(int,input('Введите дату: ').split('.'))
print(*day_name[weekday(year, month, day)])