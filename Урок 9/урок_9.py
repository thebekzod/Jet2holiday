# # class User:
# #     name = 'Jordan'
#
#
# class Jynko_solar_panel:
#     def __init__(self,watts,size,screen):
#         self.watts = watts
#         self.sides = size
#         self.screen = screen
#     pass
#
# panel1 = Jynko_solar_panel('700w',"2x1","one sided")
# print(panel1.watts)
# print(vars(panel1))
#     def stop(self):
#         print('Панель не работает')
#
#     Jynko_solar_panel.stop()
#
# class Comment:
#     def __init__(self,username,text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def add_age(self):
#         self.age +=1      #Добавить возраст
#     def change_age(self,new_age):
#         self.age = new_age    #Изменить возраст
#
# michael=Person('Michael',20)
# michael.add_age()   #Добавить возраст
# print(michael.name,michael.age)
#
# michael.change_age(69)      #Изменить возраст
# print(michael.name,michael.age)


# Bank account задачка
# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
#     def deposit(self, cash_amount):
#         self.balance += cash_amount
#
#     def withdraw(self,cash_amount):
#         self.balance -= cash_amount
#
#     def my_balance(self):
#         print(self.balance)
#
# John = BankAccount('John')
# John.my_balance()
#
# John.deposit(1000)
# John.my_balance()
#
# John.withdraw(300)
# John.my_balance()


class User:
    def __init__(self,name,email,age,phone_number):
        self.name=name
        self.email=email
        self.age=age
        self.phone_number=phone_number

    def change_username(self,new_username):
        self.name=new_username
    def change_email(self,new_email):
        self.email=new_email
    def change_phone_number(self,new_phone_number):
        self.phone_number=new_phone_number

thebekzod=User('thebekzod',"bekzodf@gmail.com",25,phone_number=946987898)

print(vars(thebekzod))

thebekzod.change_username('Beko55cool')

print(vars(thebekzod))