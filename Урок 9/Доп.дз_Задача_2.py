class Student:
    def __init__(self,name='Ivan',groupNumber="10A",age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age
    def getName(self):
            print (self.name)
    def getAge(self):
            print (self.age)
    def getGroupNumber(self):
            print (self.groupNumber)
    def setNameAge(self,new_age):
            self.age = new_age
    def setGroupNumber(self,new_groupNumber):
            self.groupNumber = new_groupNumber

Alex = Student('Alex F.','7B',14) #1
John = Student('John R.','8B',15) #2
Simon = Student('Simon E.','9B',16) #3
Rick = Student('Rick O.','6A',13) #4
Frank= Student('Frank S.','6C',13) #5

John.getName()
Alex.getAge()
Frank.getGroupNumber()
Rick.setNameAge(14)
Rick.getAge()
Simon.setGroupNumber('10A')
Simon.getGroupNumber()