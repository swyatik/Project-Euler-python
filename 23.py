"""PROJECT EULER"""

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
# number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundantnumbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as
# the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import time

ts = time.time()

max_num = 28123


def abundant(num):  # визначаємо всі надмірні числа від 12 до 28123
    list_abundant = []
    for i in range(11, num + 1):
        l = []
        for j in range(1, i // 2 + 1):  # визначаємо всі дільники
            if i % j == 0:
                l.append(j)
        if sum(l) > i:  # якщо сума дільників більша числа то додаємо в список
            list_abundant.append(i)

    return list_abundant


l_abundant = abundant(max_num)
l_positive = []
for i in range(1, max_num + 1):  # шукаємо числа, що не складені з двох abundant
    if i < 24:  # всі числа до 23 не можуть бути складені з abundant
        l_positive.append(i)  # додаємо їх у список
    else:
        # пробігаємось по списку abundant і шукаємо різницю
        # (з кожним елементом не більшого за число)
        # якщо різниця є у списку то зупиняємо цикл, бо число може бути
        # складене з двох abundant, інакше додаємо у список
        for j in l_abundant:
            if j < i and i - j in l_abundant:
                break
        else:
            l_positive.append(i)


print('The sum:', sum(l_positive))
print('Time seconds: %.5f' % (time.time() - ts))

# The sum:  871198282
# Time seconds: 539.49628
