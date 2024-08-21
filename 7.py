l=[1,2,3,4,5,7,8,9,10,11]
print(l)
print(l[0])
print(l[3])
print(l[4])
p=[1,'R',"Nishant Kumar",True]
print(p)
print(p[2])
print(len(p))
print(p[-2])  #len(p)-2=4-2=2 same as p[2]
print(p[len(p)-2])
print(p[4-2])
print(p[2])

if 10 in p:
    print("Yes")
else:
    print("NO")   

if "Nishant Kumar" in p:
    print("Yes")
else:
    print("NO")    

if "sha" in "Nishant Kumar":
    print("Yes")
else:
    print("No")    

print(l)
print(l[:])    #print complete list
print(l[0:12])    #Print from index 0 to (12-1)
print(l[0:12:2])  #jump index is 2


#List comprehension
lst=[i for i in range(5)]
print("List comprehension ",lst)
lst1=[i*i+10 for i in range(5)]
print(lst1)
lst2=[i for i in range(20) if i%2!=0]
print(lst2)