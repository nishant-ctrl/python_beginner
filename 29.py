# Decorators
# take a function and modify it and return

def greet(fx):
    def mfx():
        print("Start")
        fx()
        print("End")
    return mfx    

@greet                              # this syntax is same as greet(hello)()
def hello():
    print("Hello world")

# greet(hello)()    
hello()

def say_hi(fx):
    def mfx(*args , **kwargs):
        print("Hi")
        fx(*args , **kwargs)
        print("Thanks for using")
    return mfx

@say_hi
def add(a,b):
    print(a+b)        

# say_hi(add)(1,4)
add(1,4)

# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b

# print(my_function(5,6))