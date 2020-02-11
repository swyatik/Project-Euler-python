'''PROJECT EULER'''

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import time
ts = time.time()

n = 100
fact = 1
for i in range(1, n + 1):
    fact *= i

# рекурсія
'''
def fac(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * fac(n - 1)

fact = fac(n)
'''
print('the sum:', sum(int(i) for i in list(str(fact))))
print('Time seconds: %.5f' % (time.time() - ts))

# the sum: 648
# Time seconds: 0.00000