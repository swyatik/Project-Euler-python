'''PROJECT EULER'''

# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers. (numbers are in file '13.txt')

import time
ts = time.time()

sum = 0
with open('13.txt', 'r') as f:
    for line in f:
        sum += int(line)

print('the first ten digits of the sum: ', str(sum)[:10])
print('Time seconds: %.5f' % (time.time() - ts))

# the first ten digits of the sum:  5537376230
# Time seconds: 0.00000