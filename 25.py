"""PROJECT EULER"""

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21
# F9 = 34, F10 = 55, F11 = 89, F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?

import time
from itertools import permutations

ts = time.time()
n = 1000
count = 2
lf = [1, 1]

while True:
    lf.append(lf[count-1] + lf[count-2])
    if len(str(lf[count])) == n:
        break
    count += 1

print(count+1)
print('Time seconds: %.5f' % (time.time() - ts))

# 4782
# Time seconds: 0.04687