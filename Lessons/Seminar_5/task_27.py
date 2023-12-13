"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

def simple_number(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag

print(simple_number(6))

def simple_number1(n, flag=True, i=2):
    if i < n:
        if n % i == 0:
            flag = False
        return simple_number(n,flag,i+1)
    return flag

print(simple_number(7))