"""PROJECT EULER"""

# A unit fraction contains 1 in the numerator. The decimal representation
# of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

import time

ts = time.time()
value = 1
longest = 1
for i in range(3, 1000, 2):
    if i % 5 == 0:
        continue
    x = 1
    while (10**x) % i != 1:
        x += 1
    if x > longest:
        value, longest = i, x

print('value = {}, longest = {}'.format(value, longest))
print('Time seconds: %.5f' % (time.time() - ts))

value = 983, longest = 982
Time seconds: 0.12500
