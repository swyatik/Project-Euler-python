'''PROJECT EULER'''

#The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
import time

time_first = time.time()

# визначаэмо чи передане число просте
def factor(inst):
    if inst <= 1:
        return 0
    if inst % 2 == 0 and inst > 2:
        return 0
    square = int(sqrt(inst) + 1)
    for i in range(3, square):
        if inst % i == 0:
            return 0
    return 1

# 1-version шукаємо дільник та перевіряємо чи дільник простий через функц factor
def prime_factor_for(num):
    if factor(num) == 1:
        return 0
    prime_num = 0
    num_max = 0
    if num % 2 == 0:
        num_max = int(num / 2 + 1)
        prime_num = 2
        print(prime_num)
    else:
        num_max = int(num / 2 + 1)
    for i in range(3, num_max, 2):
        if num % i == 0:
            if factor(i) == 1:
                prime_num = i
                print(i)
    return prime_num


number = 131956789
number2 = 600851475143
print('The largest prime factor of the number {} is :'.format(number), prime_factor_for(number))

print('Time: %.5f' % (time.time() - time_first))


# Result: ?
# Time: ?