"""
ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0
"""

class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):

        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):

        if meal not in ("grass", "nectar"):
            print("Invalid meal type.")

        if meal == "grass":
            self.elephant += value
            self.bee -= value
        if meal == "nectar":
            self.bee += value
            self.elephant -= value

        if self.bee < 0:
            self.bee = 0
        elif self.bee > 100:
            self.bee = 100

        if self.elephant < 0:
            self.elephant = 0
        elif self.elephant > 100:
            self.elephant = 100

    def __str__(self):
        return f"bee: {self.bee}, elephant: {self.elephant}"

bee_elephant = None

while True:
    try:
        choice = int(input("\nMenu:"
                           "\n1)add"
                           "\n2)fly"
                           "\n3)trumpet"
                           "\n4)eat"
                           "\n5)exit\n"))

        if choice == 1:
            bee_value = int(input("\nBee value: "))
            elephant_value = int(input("\nElephant value: "))
            bee_elephant = BeeElephant(bee_value, elephant_value)
        elif choice == 2:
            if bee_elephant is None:
                print("First you need to add bee_elephant!")
                continue
            print(bee_elephant.fly())
        elif choice == 3:
            if bee_elephant is None:
                print("First you need to add bee_elephant!")
                continue
            print(bee_elephant.trumpet())
        elif choice == 4:
            if bee_elephant is None:
                print("First you need to add bee_elephant!")
                continue
            meal = input("\nWhich meal?(nectar or grass): ").strip()
            value = int(input("\nWhich value?: "))

            bee_elephant.eat(meal, value)
            print(bee_elephant)
        elif choice == 5:
            break

    except ValueError as ve:
        print(ve)