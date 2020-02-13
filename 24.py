"""PROJECT EULER"""

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3
# and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1
# and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time
from itertools import permutations

ts = time.time()

n = 1000000 - 1
ln = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# permutations - повертає ітератор кортежів
# перестановок які ми додаєм у список
s = list(permutations(ln))[n]

print(int(''.join([str(i) for i in s])))
print('Time seconds: %.5f' % (time.time() - ts))

# 2783915460
# Time seconds: 1.01562