# Class Methods

class Employee:
    company="APPLE"
    def __init__(self,name):
        self._name=name
    def show(self):
        print(f"Name is {self._name} and company is {self.company}")
    @classmethod
    def change_company(cls,new_name):
        cls.company=new_name


e1=Employee("Nishant")
e1.show()
e1.change_company("Tesla")   # it creates instance variable default but after using class method it goes as a class not an instance
e1.show()
print(Employee.company)

# Output before using @classmethod i.e. class method
# Name is Nishant and company is APPLE
# Name is Nishant and company is Tesla
# APPLE
# TO change class variable we have to use class method

#Output after using class method
# Class variable is changed
# Name is Nishant and company is APPLE
# Name is Nishant and company is Tesla
# Tesla