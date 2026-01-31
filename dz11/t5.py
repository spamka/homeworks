"""
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""

class SuperStr(str):

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]

    def is_repeatance(self, string):
        if not string:
            return False
        repeat_count = len(self) // len(string)
        return string * repeat_count == self

user_input = input("Enter your string: ")
sstr = SuperStr(user_input)

while True:
    try:
        choice = int(input(
            "\nChoose an option:"
            "\n1) Check if string is a repetition of another"
            "\n2) Check if string is a palindrome"
            "\n3) Exit\n"
        ))

        if choice == 1:
            pattern = input("Enter pattern to check repetition: ")
            result = sstr.is_repeatance(pattern)
            print("Result:", result)
        elif choice == 2:
            result = sstr.is_palindrom()
            print("Is palindrome:", result)
        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")
    except ValueError as ve:
        print(ve)