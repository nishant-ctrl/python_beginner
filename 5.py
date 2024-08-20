# Looping in python
name="Nishant Kumar"
for i in name:
    print(i ,end=" ")   #default end is \n
print("\n")
colors=["red" , "pink" , "black" , "Blue" , "Green"]
for i in colors:
    print(i)  
    for x in i:
        print(x)  

for k in range(5):   #range goes from 0 to 4
    print(k)
print("\n")
for k in range(2,5):
    print(k)   
print("\n")    
for k in range(1,11,3):  #range(start , stop , step)  same as for(k=1;k<11;k=k+3)
    print(k)   

count=1
while(count<10):
    print(count)
    count=count+1
else:
    print("Condition not satisfied.")

for i in range(1,15):
    if(i==11):
        break
    if(i==5):
        print("Skipped i==5")
        continue
    print("5 X",i,"=",5*i)
   
