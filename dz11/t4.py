"""
Программа с классом Sphere для представления сферы
в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты
центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с
соответствующим радиусом и центром в начале
координат
● метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
● метод get_square(), возвращающий число – площадь
внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей
сферы
● метод get_center(), возвращающий кортеж с координатами
центра сферы
● метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
● метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы
"""

import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        if radius <= 0:
            print("Radius must be positive. Default radius = 1")
            self.radius = 1
        else:
            self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        if radius <= 0:
            print("Radius must be positive. Default radius = 1")
            self.radius = 1
        else:
            self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        cx, cy, cz = self.center
        distance = math.sqrt((cx - x)**2 + (cy - y)**2 + (cz - z)**2)
        return distance <= self.radius


while True:
    try:
        x = int(input("Enter center x: "))
        y = int(input("Enter center y: "))
        z = int(input("Enter center z: "))
        radius = int(input("Enter sphere radius: "))
        sphere = Sphere(radius, x, y, z)
        break
    except ValueError as ve:
        print(ve)

while True:
    try:
        choice = int(input(
            "\nChoose an option:"
            "\n1) Get volume"
            "\n2) Get surface area"
            "\n3) Get radius"
            "\n4) Get center"
            "\n5) Set new radius"
            "\n6) Set new center"
            "\n7) Check if point is inside"
            "\n8) Exit\n"
        ))

        if choice == 1:
            print("Volume:", sphere.get_volume())
        elif choice == 2:
            print("Surface area:", sphere.get_square())
        elif choice == 3:
            print("Radius:", sphere.get_radius())
        elif choice == 4:
            print("Center:", sphere.get_center())
        elif choice == 5:
            radius = int(input("Enter new radius: "))
            sphere.set_radius(radius)
            print("Radius updated")
        elif choice == 6:
            x = int(input("Enter new x: "))
            y = int(input("Enter new y: "))
            z = int(input("Enter new z: "))
            sphere.set_center(x, y, z)
            print("Center updated")
        elif choice == 7:
            x = int(input("Enter x of point: "))
            y = int(input("Enter y of point: "))
            z = int(input("Enter z of point: "))
            if sphere.is_point_inside(x, y, z):
                print("The point is inside the sphere")
            else:
                print("The point is outside the sphere")
        elif choice == 8:
            print("Exiting program")
            break
        else:
            print("Invalid option")
    except ValueError as ve:
        print(ve)