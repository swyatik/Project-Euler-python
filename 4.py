'''PROJECT EULER'''
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers
import time

ts = time.time()
n = 999

for i in range(n, 100, -1): # перебираємо 1 множник від більшого до меншого
    ok = 1
    for j in range(i, 100, -1): # перебираємо 2 множник від більшого до меншого
        if int(str(i)[2]) > 0: # якщо 3-ій знак множника більший за 0(нуль)
            num = str(j * i)  # добуток в рядок
            if num[:3] == num[::-1][:3]: # якщо зріз перших трьох цифр = останнім оберненим цифрам то паліндром
                print('Result: {0} * {1} = {2}'.format(i, j, num))
                ok = 0
                break
    if ok == 0:
        break

print('Time seconds: %.5f' % (time.time() - ts))

#Result: 995 * 583 = 580085
#Time seconds: 0.00700
