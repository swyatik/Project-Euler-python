'''PROJECT EULER'''

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

import time
ts = time.time()

n = 1000
sum_n = list(str(2 ** n))
s = sum(int(i) for i in sum_n)

print('the sum: ', s)
print('Time seconds: %.5f' % (time.time() - ts))

# the sum:  1366
# Time seconds: 0.00000