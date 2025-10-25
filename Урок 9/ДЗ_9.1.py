class Food_summary:
    def __init__(self, country, price, calories, kg):
        self.country = country
        self.price = price
        self.calories = calories
        self.kg = kg
    def change_country(self, new_country):
        self.country = new_country

    def change_price(self, new_price):
        self.price = new_price

    def change_calories(self, new_calories):
        self.calories = new_calories

    def change_kg(self, new_kg):
        self.kg = new_kg

    def print_summary(self):
        print('Country: ', self.country)
        print('Price: ', self.price)
        print('Calories: ', self.calories)
        print('kg: ', self.kg)

    def print_summary_new(self):
        print('Country (updated): ', self.country)
        print('Price (updated): ', self.price)
        print('Calories (updated): ', self.calories)
        print('kg (updated): ', self.kg)

aubergine = Food_summary('Belgium','$2.34',"34 kcal","2,47kg")
aubergine.print_summary()

aubergine.change_country('Chile')
aubergine.change_price('20,000 сум')
aubergine.change_calories('69 kcal')
aubergine.change_kg('3,00 kg')

aubergine.print_summary_new()
print(vars(aubergine))