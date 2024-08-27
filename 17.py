#Short hand if else
a=29
b=12
print("A") if a>b else print("=") if a==b else print("B")

#same as
if(a>b):
    print("A")
elif (a==b):
    print("=")
else:
    print("B")

print(a) if a>b else print(b) if b>a else ""    
# we can use it like ternary operator
c=True if a>b else False
print(c)     