# Inheritance
# make a new class with use of old class

class employee:
    def __init__(self,name,role,salary):
        self._name=name
        self._role=role
        self._salary=salary
    def show_details(self):
        print(f"Name is {self._name} , Role is {self._role} , Salary is {self._salary}")

class Programmer(employee):
    def prog(self):
        print(f"Program used by {self._name} is default Python")



emp1=employee("Nishant","Engineer",1000)
emp1.show_details()            
emp2=Programmer("Aman","Engineer",100000)
emp2.show_details()   
emp2.prog()         
