"""
Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat)
"""

class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

factory = AnimalFactory()

animal_name = input("Input animal type (dog/cat): ").strip()
try:
    animal = factory.create_animal(animal_name)
    print(f"{animal_name.capitalize()} says: {animal.speak()}")
except ValueError as e:
    print(e)
