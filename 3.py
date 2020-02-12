"""PROJECT EULER"""

#The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt, ceil
import time

time_first = time.time()
n = 600851475143

def divisor(n):
    l = []
    for i in range(2, ceil(n**0.5)):
        if n%i == 0:
            l.append(i)
    return l

def prime(list):
    l_prime = []
    for i in list:
        l = []
        for j in range(1, i + 1):
            if i % j == 0:
                l.append(i)
        if len(l) == 2:
            l_prime.append(j)
            
    return max(l_prime)

print('The largest prime factor of the number 600851475143: ', prime(divisor(n)))

print('Time: %.5f' % (time.time() - time_first))


# The largest prime factor of the number 600851475143:  6857
# Time: 0.22700