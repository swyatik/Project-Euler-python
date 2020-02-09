'''PROJECT EULER'''

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
ts = time.time()

number = 1000000

col = (0, 0, 0)

def collatz (num): # вираховуємо послідовність Коллатца
    n = num
    l = [num]
    count = 1
    while n > 1:
        if n % 2 == 0: # якщо число парне
            n = int(n / 2)
            l.append(n)
            count += 1
        else:  # якщо число непарне
            n = int(n * 3 + 1)
            l.append(n)
            count += 1
    return num, l, count # повертаємо tuple - (число, список послідовності, # кількість цифр послідовності)

for i in range(number, 0, -1): # перебираємо всі цифри менші заданої
    c = collatz(i)
    if c[2] > col[2]: #якщо кількість цифр в послідовності більша
        col = c


print('Number: {}, amount number the longest chain: {}.'.format(col[0], col[2]))
print('Time seconds: %.5f' % (time.time() - ts))

# Number: 837799, amount number the longest chain: 525.
# Time seconds: 58.27083