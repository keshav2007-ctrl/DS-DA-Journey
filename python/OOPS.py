from random import randint
class Employee:
    language = "Python" #this is a class attribute
    salary = "120000"
    
    def GetInfo(cls): #a function always requires self to work without error
        print(f"The salary is: {cls.salary},\nThe language is: {cls.language}") #here cls will overide the instance attribute and show class attribute because of (cls.)
    
    @staticmethod
    def greet():
        print("?good Morning!")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter 
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
    def __init__(self): #this is called a Dunder method, any method starting with __ is dunder method
        print("this method automatically runs when a new opject is called")
e = Employee()
e.name = "harry Khan"
print(e.name)
e.language = "Java_Script" #this is an instance attribute, it gets priority over class attribute
e.GetInfo() #system reads this as Employee.GetInfo(e)


class train:
    def __init__(self, trainno):    
        self.trainno = trainno

    def bookings(self, fro, to):
        print(f"Your ticket for {self.trainno} from {fro} to {to} is booked")

    def GetStatus(self):
        print(f"The train {self.trainno} is running on time")

    def fare(self, fro, to):
        print(f"The fare for {self.trainno} from {fro} to {to} is {randint(222, 5555)}")

a = train(2599)
a.bookings("rampur", "khampur")
a.GetStatus()
a.fare("rampur", "khampur")

#Operator Overloading

class numbers:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num): #this is another inbuilt dunder method used to identify adding in python
        return self.n + num.n

n = numbers(1)
m = numbers(2)

print(n + m)
"""
some other example of dunder method are:
p1.__add__(p2)
p1.__sub__(p2)
p1.__mul__(p2)
p1.__truediv__(p2)
p1.__floordiv__(p2)
__str__()#this defines what happens when we run str(obj)
__len__() #this defines what happens when we run len(obj)
"""
