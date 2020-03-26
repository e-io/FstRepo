#Программа считывает с клавиатуры год, месяц день. Далее считывает временной промежуток. И в конце печатает итоговую дату.

import datetime as dt

a, b, c = input().split()

d = dt.date(int(a), int(b), int(c)) + dt.timedelta(int(input()))

print(d.year, d.month, d.day)



