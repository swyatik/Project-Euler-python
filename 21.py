'''PROJECT EULER'''

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time
ts = time.time()

a = 10000

# шукаємо суму дільників менших за число
def sum_divisors(n):
    return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

sum_amic = 0
l = []

for i in range(a, 0, -1):
    b = sum_divisors(i)
    if sum_divisors(b) == i and b != i:
        sum_amic = sum_amic + i + b
        l.append(i)
print('List of all the amicable numbers: \n', l)
print(' the sum of all the amicable numbers under 10000:', sum_amic)
print('Time seconds: %.5f' % (time.time() - ts))

# List of all the amicable numbers:
#  [6368, 6232, 5564, 5020, 2924, 2620, 1210, 1184, 284, 220]
#  the sum of all the amicable numbers under 10000: 63252
# Time seconds: 4.93158