"""
Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии
"""

class Strategy():
    def execute(self, a, b):
        pass

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b

class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError
        return a / b

class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if not self.strategy:
            raise ValueError("No strategy defined")
        return self.strategy.execute(a, b)


operations = {
    "add": Addition(),
    "subtract": Subtraction(),
    "multiply": Multiplication(),
    "divide": Division()
}

calc = Calculator()

print("Available operations: add, subtract, multiply, divide")
op = input("Enter operation: ").strip().lower()

if op not in operations:
    print(f"Operation '{op}' is not supported.")
    exit()

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        calc.set_strategy(operations[op])
        result = calc.calculate(a, b)
        print(f"Result: {result}")
        break
    except ValueError as ve:
        print(ve)