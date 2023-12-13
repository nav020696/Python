"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

my_list = [1, 2, 3, 4, 5]
k = 3
lst = my_list[k:] + my_list[:k] #решение через срезы
print(lst)

print(lst[: : -1]) #развернуть список

"""
list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1)
for i in range(k):
    list_1.append(list_1[0])
    list_1.pop(0) 
print(list_1)


list_1 = [1, 2, 3, 4, 5]
for i in range(k - 1):
    el = list_1.pop()
    list_1.insert(0, el)
print(list_1)

"""