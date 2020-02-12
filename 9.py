"""PROJECT EULER"""

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

ts = time.time()

for i in range(1, 1000):
    for j in range(i + 1, 1000):
        if i * i + j * j == (1000 - i - j) * (1000 - i - j):
            print('Result {}^2 + {}^2 = {}^2'.format(i, j, 1000 - i - j))
            print('Result {} * {} * {} = {}'.format(i, j, 1000 - i - j, i*j*(1000 - i - j)))


print('Time seconds: %.5f' % (time.time() - ts))

# Result 200^2 + 375^2 = 425^2
# Result 200 * 375 * 425 = 31875000
# Time seconds: 0.29687