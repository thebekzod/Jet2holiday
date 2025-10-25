class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def display_info(self):
        pass
class Car(Vehicle):
    def __init__(self,brand='Ford',year=2011):
        super().__init__(brand,year)
    def display_info(self):
        print(self.brand,self.year)

class Motorcycle(Vehicle):
    def __init__(self,brand='Ducatti',year=2005):
        super().__init__(brand,year)
    def display_info(self):
        print(self.brand,self.year)


print(vars(Car()))
print(vars(Motorcycle()))

bmw = Car('BMW M5',2021)
bmw.display_info()

honda = Motorcycle('Honda CB 350 DLX',2016)
honda.display_info()

