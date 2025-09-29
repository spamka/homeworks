"""
Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""

class Bus:
    def __init__(self,speed, capacity, max_speed):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.available_seats = capacity
        self.seats = {i: None for i in range(capacity)}

    def add_passenger(self, surname):
        if surname in self.passengers:
            return f"Passenger {surname} is already on the bus"

        for seat, passenger in self.seats.items():
            if passenger is None:
                self.seats[seat] = surname
                self.passengers.append(surname)
                self.available_seats = any(p is None for p in self.seats.values())
                return f"Passenger {surname} is on seat {seat}"
        self.available_seats = False
        return "There are no available seats"

    def remove_passenger(self, surname):
        for seat, passenger in self.seats.items():
            if passenger == surname:
                self.seats[seat] = None
                self.passengers.remove(surname)
                self.available_seats = True
                return f"Passenger {surname} removed from seat {seat}"
        return f"Passenger {surname} not found"

    def change_speed(self, value):
        self.speed = value
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
        return f"Current speed: {self.speed}"

    def __str__(self):
        return (f"Bus\n"
                f"Speed: {self.speed}\n"
                f"Passengers: {self.passengers}\n"
                f"Seats:{self.seats}\n"
                f"Available seats:{self.available_seats}")


bus = None
while True:
    try:
        choice = int(input("\nMenu:"
                           "\n1. Create bus"
                           "\n2. Add passenger"
                           "\n3. Remove passenger"
                           "\n4. Change speed"
                           "\n5. Show"
                           "\n6. Exit\n"))
        if choice == 1:
            max_speed = int(input("\nMax Speed:"))
            speed = int(input("\nSpeed:"))
            while speed > max_speed:
                speed = int(input("\nSpeed:"))
            capacity = int(input("\nCapacity:"))
            bus = Bus(speed, capacity, max_speed)
        elif choice in [2, 3, 4, 5] and bus is None:
            print("Choose option 1")
        elif choice == 2:
            surname = input("\nSurname:")
            print(bus.add_passenger(surname))
        elif choice == 3:
            surname = input("\nSurname:")
            print(bus.remove_passenger(surname))
        elif choice == 4:
            changed_speed = int(input("\nSpeed:"))
            print(bus.change_speed(changed_speed))
        elif choice == 5:
            print(bus)
        elif choice == 6:
            break
    except ValueError as ve:
        print(ve)
