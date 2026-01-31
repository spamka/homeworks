"""
Создайте класс Soda (газировка). Для инициализации
есть параметр, который определяет вкус газировки. При
инициализации этот параметр можно задавать, а можно и не
задавать. Реализовать метод строковой репрезентации,
который возвращает строку вроде «У вас газировка с
<клубничным> вкусом», если вкус задан. Если вкус не задан,
метод должен возвращать строку «У вас обычная газировка»
"""

class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You have soda with {self.taste} taste"
        else:
            return "You have soda without taste"

soda = None
while True:
    try:
        a = int(input("1)add taste\n2)skip\n3)exit\n"))
        if a == 1:
            taste = input("Input taste: ")
            soda = Soda(taste)
            break
        elif a == 2:
            soda = Soda()
            break
        elif a == 3:
            break
    except ValueError as ve:
        print(ve)

if soda:
    print(soda)