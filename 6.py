def add(a,b):
    return a+b

print(add(15,8))
print(add(1,4))

def greet():
    print("Hello User")

greet()

def sum(a=2 , b=5):  #default arguments
    return a+b
print(sum())
print(sum(9,7))
print(sum(3))  #b is default 5
print(sum(b=10))  #a is default 2

#Keyword arguments
print(sum(b=10,a=12))  #order change

def mul(a , b=2):
    return a*b

print(mul(4)) #a is required argument

#Variable length argument
def average(*numbers):
    avg=0
    for i in numbers:
        avg+=i
    return avg/len(numbers)    

print(average(1,2))
print(average(1,2,3))
print(average(1,2,3,4))