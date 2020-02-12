"""PROJECT EULER"""

# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance
# with British usage.

import time
from num2words import num2words
ts = time.time()


n = 1000
sum_word = 0

def amount(number):
    word = num2words(number).replace(' ', '')
    return len(word.replace('-', ''))

for i in range(1, n + 1):
    sum_word = sum_word + amount(i)

print('the amount of letters: ', sum_word)
print('Time seconds: %.5f' % (time.time() - ts))

# the amount of letters:  21124
# Time seconds: 0.06904