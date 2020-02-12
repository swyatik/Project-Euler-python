"""PROJECT EULER"""
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers
import time
ts = time.time()

n = 999
product_max = 0
n1 = 0
n2 = 0
for i in range(n, 100, -1):  # перебираємо 1 множник від більшого до меншого
    for j in range(i, 100, -1):  # перебираємо 2 множник від більшого до меншого
        if int(str(j)[2]) > 0 and int(str(i)[2]) > 0:
            product = i * j
            if str(product) == str(product)[::-1]:  # якщо паліндром то порывнюэмо та записуємо
                if product > product_max:
                    product_max = product
                    n1 = i
                    n2 = j


print('The largest palindrome {} * {} = {}'.format(n1, n2, product_max))
print('Time seconds: %.5f' % (time.time() - ts))

# The largest palindrome 993 * 913 = 906609
# Time seconds: 0.71875
