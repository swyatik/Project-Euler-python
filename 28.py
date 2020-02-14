"""PROJECT EULER"""

# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
""" залежність діагоналей можна вивести формулою:
    n^2+(n^2-(n-1))+(n^2-(n-1)-(n-1))+(n^2-(n-1)-(n-1)-(n-1)) = 4n^2-6n+6, 
    де n - розмір матриці (наприклад: для 3х3 n=3, для 1001х1001 n=1001)"""

import time

ts = time.time()

n = 1001
sum_d = 1

for i in range(3, n + 1, 2):
    sum_d += (4 * i * i - 6 * i + 6)

print(sum_d)
print('Time seconds: %.5f' % (time.time() - ts))

# 4782
# Time seconds: 0.04687