"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Пример

На входе:
print_operation_table(lambda x, y: x * y, 3, 3)

print_operation_table(lambda x, y: x + y, 4, 4)
На выходе:
1 2 3
2 4 6 
3 6 9

1 2 3 4
2 4 5 6
3 5 6 7
4 6 7 8
"""

def print_operation_table(operation, num_rows, num_columns):
    if (num_rows < 2):
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        res = [[1] * num_columns for i in range(num_rows)]
        for i in range(num_columns):
            res[0][i] = i + 1
        for i in range(num_rows):
            res[i][0] = i + 1
        for i in range(1, num_rows):
            for j in range(1, num_columns):
                res[i][j] = operation(res[i][0], res[0][j])
        print_list(res)
        

def print_list(my_list):
    for row in my_list:
        string = ""
        for el in row:
            string += str(el)
            string += ' '
        print(string[:-1])
        

print_operation_table(lambda x, y: x / y, 4, 4)


