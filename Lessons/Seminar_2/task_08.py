"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""

list1 = [-20, 30, -40, 50, 10, -10]
length = 0
max_length = 0
for num in list1:
    if num > 0:
        length += 1
    else:
        length = 0
    if length > max_length:
        max_length = length
print(max_length)

"""
n = 6
count = 0
count_final = 0
for i in range(n):
    temper = int(input(f'Введите среднесуточную температуру {i + 1} дня '))
    if temper > 0:
        count += 1
    else:
        count = 0
    if count_final < count:
        count_final = count
print(f'Самая длинная оттепель {count_final} дней')
"""