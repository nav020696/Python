"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
n = 7

"""
def fibonacci(n):
    if n < 3:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = 7
print(fibonacci(n))

fib1, fib2 = 0, 1
for i in range(0, n):
    fib1, fib2 = fib2, fib2 + fib1
print(fib2)

"""

def fibonachi(n):
    if n == 1:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


print(fib(n))
print(fibonachi(n))