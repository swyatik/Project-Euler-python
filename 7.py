"""PROJECT EULER"""

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import time
from math import sqrt

ts = time.time()


def factor(inst):
    if inst == 2:
        return 1
    if inst % 2 == 0 and inst > 2:
        return 0
    square = int(sqrt(inst) + 1)
    for i in range(3, square):
        if inst % i == 0:
            return 0
    return 1

max = 2
number = 0

while number < 10001:
    if factor(max) == 1:
        number += 1
    max += 1

print('the 10 001st prime number: ', max - 1)

print('Time seconds: %.5f' % (time.time() - ts))

# the 10 001st prime number:  104743
# Time seconds: 0.31250