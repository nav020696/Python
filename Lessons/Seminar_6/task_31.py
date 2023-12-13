"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

Ввод:
7
3 1 3 4 2 4 12

6
4 15 43 1 15 1

Вывод:
3 3 2 12
"""

lst_1 = "3 1 3 4 2 4 12".split()
lst_2 = "4 15 43 1 15 1".split()

lst = list(item for item in lst_1 if item not in lst_2)
print(lst)




import random
def create_arr():
    n = int(input("Введите число элементов: "))
    arr = [random.randint(0, 9) for x in range(0,n)]
    print(*arr)
    return arr

arr_n = create_arr()
arr_m = create_arr()

for i in arr_n:
    if i not in arr_m:
        print(i, end=" ")