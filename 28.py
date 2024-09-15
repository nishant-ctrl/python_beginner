# Constructers

# class person:
#     name="Nishant"
#     roll=57
#     salary=100
#     def info(self):
        # print(f"Name is {self.name} , Roll is {self.roll} and salary is {self.salary}")

class person:
    def __init__(self,n,r,s):         # this calls everytime
        self.name=n
        self.roll=r
        self.salary=s
    def info(self):
        print(f"Name is {self.name} , Roll is {self.roll} and salary is {self.salary}")

a=person("Nishant",57,100)   # a is passed as self
a.info()
b=person("Aman" , 98 , 1000)
b.info()