# Custom errors raising

a=int(input("Enter a number between 10 and 20: "))
if(a<10 or a>20):
    raise ValueError("Number should be in b/w 10 and 20")

# we can raise custom error with classes


