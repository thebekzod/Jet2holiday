# class Animal:
#     def make_sound(self,s):
#         print(s)
#
# class Horse(Animal):
#     pass
#
# pony = Horse()
# pony.make_sound('Igogo')
#

# class Parent:
#     def calculator(self,a,b):
#         print(a*b)
#
# class Child(Parent):
#     pass
#
# Grandson=Child()
# Grandson.calculator(45,2)


# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color = color
#         self.year = year
#
# class Supercar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor
#
#
# amg1=Supercar('Amg One', 'black', 2020, 'Petronas')
# print(vars(amg1))

# class Animal:
#     @classmethod
#     def make_sound(cls,s):
#         print(s)
#
# Animal.make_sound('Woof')

# class Worker:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
# class HR(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#     def HR_get_position(self, worker):
#          return worker.name, worker.position   #worker не понял где связь
#
# John = Worker('John', 'lawyer')
# Christopher = Worker('Christopher', 'manager')
# Alexander = HR('Alexander', 'HR')
#
# print(Alexander.HR_get_position(John))
# print(Alexander.HR_get_position(Christopher))

class Player:
    def __init__(self, speed, stamina,power,accuracy):
        self.speed = speed
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy

class Striker(Player):
    def __init__(self, speed, stamina, power,accuracy):
        super().__init__(speed,stamina,power,accuracy)
    def score_goal(self):
        print('Забил гол!')

class Defender(Player):
    def __init__(self, speed, stamina, power,accuracy):
        super().__init__(speed,stamina,power,accuracy)
    def made_tackle(self):
        print('Постелился в подкат!')

class Midfielder(Player):
    def __init__(self, speed, stamina, power,accuracy):
        super().__init__(speed,stamina,power,accuracy)
    def made_assist(self):
        print('Сделал ассист!')

class Goalkeeper(Player):
    def __init__(self, speed, stamina, power,accuracy):
        super().__init__(speed,stamina,power,accuracy)

    def made_save(self):
        print('Сделал сейв!')

Striker.score_goal(1)
Defender.made_tackle(1)
Midfielder.made_assist(1)
Goalkeeper.made_save(1)