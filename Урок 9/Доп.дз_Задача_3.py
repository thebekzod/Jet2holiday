class Math:
    def __init__(self, a=55, b=66):
        self.a = a
        self.b = b
    def addition(self,a,b):
        print(a+b)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        print(a/b)
    def subtraction(self,a,b):
        print(a-b)

calculator = Math()

calculator.addition(5,10)
calculator.multiplication(5,10)
calculator.division(10,5)
calculator.subtraction(10,5)