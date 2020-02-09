'''PROJECT EULER'''

# Starting in the top left corner of a 2×2 grid, and only being
# able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

import time
ts = time.time()

n = 20
l = [[1] * (n + 1)]

for i in range(n):
    l.append([1])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        l[i].append(l[i - 1][j] + l[i][j - 1])


print('There are {} routes'.format(l[n][n]))
print('Time seconds: %.5f' % (time.time() - ts))

# There are 137846528820 routes
# Time seconds: 0.00000