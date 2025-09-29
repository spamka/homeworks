"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""

def nums(values):
    while True:
        for value in values:
            yield value

while True:
    try:
        count = int(input("How many numbers? "))
        if count <= 0:
            count = int(input("Enter a positive number: "))

        values = [1, 2, 3]
        generator = nums(values)

        for _ in range(count):
            print(next(generator), end="-")
        break
    except ValueError as ve:
        print(ve)