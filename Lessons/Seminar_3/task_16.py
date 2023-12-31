"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

list_num = [0, -1, 5, 2, 3, 4, 3]
count = 0
for i in range(1, len(list_num)):
    if list_num[i] > list_num[i-1]:
        count += 1
print(count)


"""
Автоматическое форматирование кода в Visual Studio Code выполняется следующими комбинациями:
Windows: Shift + Alt + F.
Mac: Shift ⇧ + Option ⌥ + F.
Ubuntu: Ctrl + Shift + I.
"""