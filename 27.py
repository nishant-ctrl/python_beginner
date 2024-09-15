# OOPS start


class person:
    name="Nishant"
    roll=57
    salary=100
    def info(self):
        print(f"Name is {self.name} , Roll is {self.roll} and salary is {self.salary}")


a=person()
print(a.name , a.roll , a.salary)
a.info()
a.name="Aman"
a.roll=98
a.salary=10000
print(a.name , a.roll , a.salary)
a.info()

# Method means function jo class ke andar hai
# self means wo object jiske liye Method call ho rha hai
