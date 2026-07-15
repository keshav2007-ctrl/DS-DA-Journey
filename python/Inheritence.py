class Employee: #this can be called as base/parent class
    company = "ITC"

    def show(self):
        print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}") #this method(and any other method that might be addded to this class in future) has been inherited by programmer class.

"""
class Programmer:
    company = "ITC Infotech"

     def show(self):
        print(f"The name of the employee is {self.name}, The salary of the employee is {name.salary}") #here we had to physically copy and paste the methods of employee class

    def showLang(self):
        print(f"The employee {self.name} is good in {self.language} language")
"""

class programmer(Employee): #here progrmmer class will inherit all the methods of employee class and can have its own methods alongisde, this is also know as derived/child class
    company = "ITC Infotech"

    def showLang(self):
        print(f"The employee {self.name} is good in {self.language} language")

a = Employee()
b = programmer()

print(a.company, b.company)

#there are 3 types of inheritence: single, multiple, multilevel (given above is an example of single inheritence other two are down below)

class Employee: #this can be called as base/parent class
    company = "ITC"
    name = ""

    def show(self):
        print(f"The name of the employee is {self.name}\nThe company of the employee is {self.company}") #this method(and any other method that might be addded to this class in future) has been inherited by programmer class.

class coder:
    language = "Python"
    def printLang(self):
        print(f"Out of all the languages this is yours {self.language}")

class programmer(Employee, coder): #here progrmmer class will inherit all the methods of employee class aswell as coder class.
    company = "ITC Infotech"

    def showLang(self):
        print(f"The employee {self.company} is good in {self.language} language")

a = Employee()
b = programmer()

print(a.company, b.company)
b.show()
b.printLang()
b.showLang()

#Multi-Level Inheritence
class Employee: #this can be called as base/parent class
    company = "ITC"
    name = ""

    def __init__(self):
        print("This is employee") #this method(and any other method that might be addded to this class in future) has been inherited by programmer class.
    a = 1

class Programmer(Employee): #this is the 1st level of inheritence
    language = "Python"
    def __init__(self):
        print("This is Programmer")
    b = 2

class Manager(Programmer): #this is the second level of inheritence(it will inherite anything that its parent class has inherited)
    company = "ITC Infotech"

    def __init__(self):
        super().__init__() #This will run the parent class cunstructor as well
        print("This is Manager")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c) #if i only run this it will also run programmer class's constructor because of super().__init__()


class Employee:
    salary = 234
    increment = 20

    @property
    def SalaryAfterIncrement(self):
        return self.salary + (self.salary*self.increment/100)

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):

        self.increment = ((salary/self.salary)-1)*100
    

e = Employee()
e.SalaryAfterIncrement = 280.9
print(e.increment)

