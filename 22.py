"""PROJECT EULER"""

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import time
ts = time.time()

total = 0

with open('names_22.txt', 'r') as f:  # відкриваємо файл для читання
    file = sorted(f.read().replace('"', '').split(','))  # читаємо, прибираємо лапки, розбиваємо рядок
    for i in range(len(file)):
        # проходимо по кожному слову, кожну літеру перетворюємо в верхній регістр,
        # якщо потрібно, повертаємо відповідник літері в таблиці
        # ASCII(віднімаємо 64, щоб привести до А=1, В=2...) далі по умові задачі
        total = total + ((i + 1) * sum(ord(j.upper())-64 for j in file[i]))




print('The total of all the name scores in the file: ', total)
print('Time seconds: %.5f' % (time.time() - ts))

# The total of all the name scores in the file:  871198282
# Time seconds: 0.01562