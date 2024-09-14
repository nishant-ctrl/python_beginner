# Lambda function   lambda <argument>:<expression>

# def double(x):
#     return x*2

double=lambda x:x*2
cube=lambda x:x**3
print(double(5))
print(f"cube of 3 is {cube(3)}")
# we can pass function to a function
def app(fx,value):
    return 10+fx(value)

print(app(lambda x:x**2 , 5))