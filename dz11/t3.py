"""
 Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета.
"""

class Car:
    def __init__(self, color, year, car_type):
        self.color = color
        self.year = year
        self.car_type = car_type

    def start(self):
        print("The car is started")

    def stop(self):
        print("The car is stopped")

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_type(self, car_type):
        self.car_type = car_type

    def __str__(self):
        return f"The car: {self.color}, {self.year}, {self.car_type}"

try:
    color = input("Color: ")
    year = int(input("Year: "))
    type = input("Type: ")
except ValueError as e:
    print(e)

car = Car(color, year, type)
car.start()
print(car)
car.stop()
