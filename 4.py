print("Enter time in 24 hours format: ")
h=int(input("Enter hours: "))
m=int(input("Enter minutes: "))
s=int(input("Enter seconds: "))
if(h<12 and h>=0):
    print("Good Morning")
elif(h>=12 and h<18):
    print("Good Afternoon")
elif(h>=18 and h<=24):
    print("Good Night")
else:
    print("Wrong Data")

import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(timestamp)
if(hour>=5 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternoon")
elif(hour>=17 and hour<20):
    print("Good Evening")
elif((hour>=20 and hour<=24) | (hour>=0 & hour<5)):
    print("Good Night")            

x=int(input("Enter value of x: "))
match x:
    case 0:
        print("X is 0")
    case _ if(x!=90):
        print("X is not 90")
    case _ if(x==50):
        print("X is 50")
    case _:
        print(x)
