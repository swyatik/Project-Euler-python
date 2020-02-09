'''PROJECT EULER'''

# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.

end = 4000000
a = 1
b = 2
next = 0
sum = 2

while True:
    print(a)
    if next > end:
        break
    else:
        if next%2 == 0:
            sum += next
        next = a + b
        a = b
        b = next

print('the sum of the even-valued terms =', sum)