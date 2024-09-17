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

# Access Modifiers not present in python But people use these as convention
# 1.Public => can be accessed outside the class (normal that we define)
#2.Private => should be initialised with double underscore '__'
#3.Protected => can be accesed within a class or its subclass. it is also a convention . use "_name"

class student:
    def __init__(self):
        self.__name="Nishant"
        self._name="Kumar"

s1=student()
print(s1._name)
#print(s1.__name)   can't be accessed like this to access do  s1._student__name
print(s1._student__name) 
# This is known as Name Mangling
# __name is renamed as _student__name so that it can't be modified accidently by user
print(s1.__dir__())
