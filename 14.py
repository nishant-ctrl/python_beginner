# Dicionary
dic={"Name":"Nishant" , "Roll":57 , "Branch":"ECE"}

print(dic["Name"])
print(dic["Roll"])
print(dic["Branch"])

emp={11:"Nishant" , 22:"Ravi" , 12:"Shubham"}
print(emp[11] , emp[22] , emp[12])

print(dic)

# print(dic["name"])  #if name is not present in dict then it throws error
print(dic.get("name"))   #if name is not present then it prints "None"

# to access all keys
print(emp.keys())
print(emp.values())
#   or
for key in emp.keys():
    print(emp[key])
    print(f"The value corresponding to {key} is {emp[key]}")

print(emp.items())
for key,value in emp.items():
    print(f"The value corresponding to {key} is {value}")


# Dictionary menthods
ep1={100:23 , 101:56 , 102:94}
ep2={90:34 , 94:100 , 57:80}  #repetition not allowed like in sets
print(ep1)
ep1.update(ep2)  #add elements of ep2 to ep1
print(ep1)
ep2.clear()
print(ep2)
print("Before pop",ep1)
ep1.pop(100)
print("After pop key",100 ,ep1)
# popitem pop key and value from last
print("Before popitem",ep1)
ep1.popitem()
print("After popitem",ep1)
# deleting a dict
inp={1:10 , 2:20 , 3:30}
print(inp)
del inp[2]  # delete key=2  
print(inp)
del inp # deletes whole dict