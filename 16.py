# Custom errors raising

a=int(input("Enter a number between 10 and 20: "))
if(a<10 or a>20):
    raise ValueError("Number should be in b/w 10 and 20")

# we can raise custom error with classes
i=input("Enter no b/w 10 and 20: ")
if(i=="quit"):
    exit()
elif(i.isalpha()):
    print("Please Enter an integer value.")
elif(int(i)<10 or int(i)>20):
    raise ValueError("Number should be in b/w 10 and 20")
else:
    print("Input is accepted.")        

