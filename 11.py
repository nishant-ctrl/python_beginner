# DocStrings

def add(a,b):
    '''Takes two no.. a and b and returns the sum a+b'''
    return a+b

def square(n):
    '''Takes a no. and returns square of it'''
    return (n**2)

print("Sum is :",(add(7,8)))
print(add.__doc__)
print("Square of",5,"is",square(5))
print(square.__doc__)