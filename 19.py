"""PROJECT EULER"""

# You are given the following information, but you may prefer
# to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import time
from calendar import weekday
ts = time.time()

date_start = [1901, 1, 1]
date_end = [2000, 12, 1]
count = 0
for i in range(date_start[0], date_end[0] + 1): # проходимо по роках
    for j in range(1, 13): # проходимо по місяцях
        if weekday(i, j, 1) == 6: # якщо 1 день місяця Неділя то додаємо
            count += 1

print('Sundays fell on the first of the month: ', count)
print('Time seconds: %.5f' % (time.time() - ts))

# Sundays fell on the first of the month:  171
# Time seconds: 0.00000