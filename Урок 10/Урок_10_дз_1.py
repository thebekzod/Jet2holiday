class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Woof!')
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
class Cow(Animal):
    def make_sound(self):
        print('Mooo!')

Шарик=Dog()
Шарик.make_sound()

Барсик=Cat()
Барсик.make_sound()

Анатолий=Cow()
Анатолий.make_sound()

