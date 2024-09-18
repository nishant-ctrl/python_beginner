# Class method as alternative constructors

class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary

    @classmethod
    def fromstr(cls , str):
        return cls(str.split("-")[0] , str.split("-")[1])

e1=Employee("Nishant",100)   # This is normal case no problen
print(e1._name)
print(e1._salary)

# Suppose that data is in formar of str="Nishant-100"
# We have to parse string first and then store 
# We have to use class methos as alternative constructors
string="Aman-100"
print(string.split("-"))
# e2=Employee(str.split("-")[0] , str.split("-")[1])     # It works but it is not good for big programs
e2=Employee.fromstr(string)
print(e2._name)
print(e2._salary)

# We can use class methos as alternative constructors
