"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.
"""

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

while True:
    try:
        limit = int(input("Enter the Fibonacci number: "))
        if limit < 0:
            limit = int(input("Enter a positive number: "))

        for value in fibonacci(limit):
            print(value, end=" ")
        break
    except ValueError as ve:
        print(ve)
