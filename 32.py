# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
 
min = 2
max = 15
data = [randint(1, 10) for _ in range(20)]
print("Массив: ", data, sep='\n')
indexes = [i for i, j in enumerate(data) if min <= j <= max]
print("Индексы: ", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Остальные элементы: ", data, sep='\n')
print("Обязательные элементы: ", result, sep='\n')