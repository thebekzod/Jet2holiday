class Car:
    def __init__(self, color,type,year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def setYear(self,new_year):
        self.year = new_year
    def setType(self,new_type):
        self.type = new_type
    def setColor(self,new_color):
        self.color = new_color

Xiaomi = Car('Brooklyn Grey','Crossover', '2025')

Xiaomi.start()
Xiaomi.stop()
Xiaomi.setYear('2026')
Xiaomi.setType('Crossover EV')
Xiaomi.setColor('Sky Blue')

print(vars(Xiaomi))