#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# a = int(input('Введите первый элемент: '))
# l = a
# n = int(input('Введите шаг: '))
# k = n
# d = int(input('Введите количество: '))
# for i in range(d):
#     for a in range(n):
#         a1 = a + n
#         an = a1 + (n-1) * d
#         i += 1
# print(l, k, an)

# 2 решение

# a = int(input('Введите первое число: '))
# d = int(input('Введите шаг: '))
# n = int(input('Введите количество элементов: '))

# progression = [a + i * d for i in range(n)]
# print(progression)

# 3 решение

a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)