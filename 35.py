# instance variables and class variables

class Employee:
    company_name="Apple"
    no_of_employe=0
    def __init__(self,name):
        self._name=name
        Employee.no_of_employe+=1
    def show_info(self):
        print(f"Name of employee is {self._name} in the company {self.company_name}")

emp1=Employee("Nishant")
emp1.show_info()               # Both are same        
# Employee.show_info(emp1)  
emp2=Employee("Aman")

emp2.show_info()                      

# instance variable is associated with instance i.e. emp1._name
# class variable is common to all instances i.e. company_name
# class variable is shared by all instances

emp1.company_name="Apple India"     # craetes instance variable for emp1
emp1.show_info()                    # if instance variable is present then it will show 
emp2.show_info()                    # but if instance variable is not present then class variable is shown

print(Employee.company_name)
Employee.company_name="Samsung"
print(Employee.company_name)

emp1.show_info()
emp2.show_info()                    