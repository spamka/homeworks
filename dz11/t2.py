"""
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""

class Math:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return print("+:", num1 + num2)

    def sub(self, num1, num2):
        return print("-:", num1 - num2)

    def multiply(self, num1, num2):
        return print("*:", num1 * num2)

    def divide(self, num1, num2):
        try:
            return print("/:", num1 / num2)
        except ZeroDivisionError as e:
            print(e)

def input_num():
    while True:
        try:
            num1 = float(input("Input num1: "))
            num2 = float(input("Input num2: "))
            return num1, num2
        except ValueError as ve:
            print(ve)


num1, num2 = input_num()
math = Math()
math.add(num1, num2)
math.sub(num1, num2)
math.multiply(num1, num2)
math.divide(num1, num2)
