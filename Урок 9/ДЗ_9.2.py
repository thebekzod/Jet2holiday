class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

andrey = Person('Андрюха', 20)
print(andrey.name, andrey.age)

sasha = Person('Сашка', 24)
print(sasha.name, sasha.age)

gregoriy = Person('Гриша', 19)
print(gregoriy.name, gregoriy.age)

print(vars(gregoriy),vars(sasha),vars(andrey))



