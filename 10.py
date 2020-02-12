"""PROJECT EULER"""

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

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

n = 2000000
max = 2
sum = 0

while True:
    if factor(max) == 1 and max < n:
        sum += max
    if max > n:
        break
    max += 1

print('the sum of all the primes below two million: ', sum)
print('Time seconds: %.5f' % (time.time() - ts))

# the sum of all the primes below two million:  142913828922
# Time seconds: 21.20473