'''PROJECT EULER'''

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

import time

ts = time.time()
n = 20
max = n


while True:
    ok = 0
    for i in range(2, n + 1):
        if max % i > 0:
            break
    else:
        ok = max

    if ok > 0:
        print('Result: {}'.format(ok))
        break
    max += 1


print('Time seconds: %.5f' % (time.time() - ts))

# result:232792560
# Time seconds: 208.46684