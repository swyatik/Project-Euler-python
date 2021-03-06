"""PROJECT EULER"""

# The sequence of triangle numbers is generated by adding the
# natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five
# hundred divisors?

import time
from math import ceil
ts = time.time()

n = 50

triangle_numbers = 1
c = 1

def divisor(number, num):
    count = 1
    for i in range(1, ceil(number*0.5)):
        if number % i == 0:
            count += 1
            if count > num:
                break
    return count

while True:
    if divisor(triangle_numbers, n) > n:
        break
    c += 1
    triangle_numbers += c

print('The value: ', triangle_numbers)
print('Time seconds: %.5f' % (time.time() - ts))

"""
# не моя реалізація (з інтернету) швидша в 10 разів
def proverka(n):
    c = math.ceil(n**0.5)
    if c*c == n:
        return True
    else:
        return False

def func(m):
    x = 3
    n = 2
    while n<=m:
        n = 2
        s = sum([c for c in range(1,x+1)])
        for i in range(2,math.ceil((s**0.5))):
            if s%i == 0:
                n+=2
        if proverka(s):
            n+=1
        x+=1
    return s
print(func(500))

"""
