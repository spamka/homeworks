"""
Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене
"""

class Product:
    def __init__(self, name, price, store):
        self.__name = name
        self.__price = price
        self.__store = store

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_store(self):
        return self.__store

    def __str__(self):
        return f"Product: {self.__name}, Price: {self.__price}, Store: {self.__store}"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def remove_product_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                self.__products.remove(product)
                return True
        return False

    def show_by_index(self, index):
        if 0 <= index < len(self.__products):
            return str(self.__products[index])
        return "Invalid index"

    def show_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return str(product)
        return "Product not found"

    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda p: p.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.get_price())

    def sum_prices(self):
        total = 0
        for product in self.__products:
            total += product.get_price()
        return total

    def show_all(self):
        return "\n".join(str(p) for p in self.__products)

warehouse = Warehouse()

while True:
    try:
        choice = int(input("\nMenu:"
                           "\n1) Add product"
                           "\n2) Remove product by name"
                           "\n3) Show product by index"
                           "\n4) Show product by name"
                           "\n5) Sort products by name"
                           "\n6) Sort products by store"
                           "\n7) Sort products by price"
                           "\n8) Sum of all product prices"
                           "\n9) Show all products"
                           "\n0) Exit\nYour choice: "))

        if choice == 1:
            try:
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                store = input("Enter store name: ")
                if not name.strip() or not store.strip():
                    print("Name and store cannot be empty.")
                elif price < 0:
                    print("Price cannot be negative.")
                elif warehouse.show_by_name(name) != None:
                    print("Product with this name already exists.")
                else:
                    warehouse.add_product(Product(name, price, store))

            except ValueError:
                print("Invalid price input.")
        elif choice == 2:
            name = input("Enter product name to remove: ")
            print("Product removed." if warehouse.remove_product_by_name(name) else "Product not found.")
        elif choice == 3:
            index = int(input("Enter product index: "))
            print(warehouse.show_by_index(index))
        elif choice == 4:
            name = input("Enter product name: ")
            print(warehouse.show_by_name(name))
        elif choice == 5:
            warehouse.sort_by_name()
            print("Products sorted by name.")
        elif choice == 6:
            warehouse.sort_by_store()
            print("Products sorted by store.")
        elif choice == 7:
            warehouse.sort_by_price()
            print("Products sorted by price.")
        elif choice == 8:
            print(f"Total price of all products: {warehouse.sum_prices()}")
        elif choice == 9:
            print("All products:\n" + warehouse.show_all())
        elif choice == 0:
            break
    except ValueError:
        print("Invalid input.")