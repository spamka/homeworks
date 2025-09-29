"""
Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza."""

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = ""
        self.pepperoni = ""
        self.mushrooms = ""
        self.onions = ""
        self.bacon = ""

    def __str__(self):
        ingredients = []
        if self.cheese: ingredients.append("cheese")
        if self.pepperoni: ingredients.append("pepperoni")
        if self.mushrooms: ingredients.append("mushrooms")
        if self.onions: ingredients.append("onions")
        if self.bacon: ingredients.append("bacon")
        if ingredients:
            return f"Pizza(size={self.size}, ingredients={', '.join(ingredients)})"
        else:
            return f"Pizza(size={self.size}, bread)"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        size = input("Input the size of the pizza (small, medium, large): ").lower()
        if size in ["small", "medium", "large"]:
            self.pizza.size = size
        else:
            print("Invalid size. Defaulting to 'medium'.")
            self.pizza.size = "medium"
        return self

    def add_cheese(self):
        self.pizza.cheese = input("Add cheese? (yes/no): ").lower() == "yes"
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = input("Add pepperoni? (yes/no): ").lower() == "yes"
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = input("Add mushrooms? (yes/no): ").lower() == "yes"
        return self

    def add_onions(self):
        self.pizza.onions = input("Add onions? (yes/no): ").lower() == "yes"
        return self

    def add_bacon(self):
        self.pizza.bacon = input("Add bacon? (yes/no): ").lower() == "yes"
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .set_size()
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .add_onions()
                .add_bacon()
                .build())

builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)
