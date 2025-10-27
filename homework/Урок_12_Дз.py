#2. Переменные и тип данных
try:
    number = int(input("Введите ваше число: "))
    if number % 2 == 0:
        print("Ваше число чётное")
    else:
        print("Ваше число нечётное")
except ValueError:
    print("Ошибка! Введите целое число.")

#3. Список
names =['Aleksey', 'Ivan', 'Sergey', 'Dmitriy']
names.reverse()
names.append("Grisha")
print(names)

#4. Цикл for
names =['Aleksey', 'Ivan', 'Sergey', 'Dmitriy']
for i in names:
    print(i,"***здесь должна быть фамилия***")

#5. List comprehension
nums = [a for a in range(51)]
chotnie = [num for num in nums if num%2==0]
print(chotnie)
nechotnie = [num for num in nums if num%2!=0]
print(nechotnie)

#6. Словари
class_list={'Aleksey':"1A", "Ivan":"2B", "Sergey":"3G", "Dmitriy":"2D"}
print(class_list['Aleksey'])
print(class_list.keys())
print(class_list.values())

#7. Функции
def print_everything_above():
    print(names)
    print(chotnie)
    print(nechotnie)
    print(class_list)

print_everything_above()

#8. Анонимные функции
kvadrat_chisla = lambda x: x**2
print(kvadrat_chisla(25))

#9 & #10. Классы & Наследование
class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def graduate_student(self):
        print(f'{self.name} окончил университет!')

class Pupil(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    def graduate_pupil(self):
        print(f'{self.name} окончил школу!')

maks=Student("Максим", 22)
gleb=Pupil("Глеб", 18)
maks.graduate_student()
gleb.graduate_pupil()