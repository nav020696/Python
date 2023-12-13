"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""
import math

list_1 = [8, 9, 2]
k = 8

res_element = list_1[0]
differense = math.fabs(k - list_1[0])

for i in range(1, len(list_1)):
    if math.fabs(k - list_1[i]) < differense:
        differense = math.fabs(k - list_1[i])
        res_element = list_1[i]
print(res_element)

    