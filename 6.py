'''PROJECT EULER'''

# The sum of the squares of the first ten natural numbers is,
#
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
#
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

import time

ts = time.time()
s1 = 0
s2 = 0
for i in range(1, 101):
    s1 = s1 + i * i
    s2 += i

print('the difference between the sum: ', (s2 * s2 - s1))

print('Time seconds: %.5f' % (time.time() - ts))

# the difference between the sum:  25164150
# Time seconds: 0.00000