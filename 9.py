#tuples is same as list but cant be changed
tup=(1,2,3,4,5,"Nishant")
print(tup)
print(type(tup))
print(tup[0])
# tup[0]=34  throws  error i.e. tuple can't be changed

p=(4)
print(p)
print(type(p))   #tuple with one element is int
#to solve this we must use a comma like    p=(1,)
p=(4,)
print(p)
print(type(p))

if 343 in tup:
    print("Yes")
else:
    print("No")

#we can't add elements to tuples to do this first convert tuples->list add and then list->tuple
temp=list(tup)
temp.append("Kumar")
temp.pop(0)  # 0 is index no.
temp.append(89)
tup=tuple(temp)
print(tup)            

# concatenate tuple
k=(9,8,7,8,9,0,1,2,4,6,4,3,5)
new_tup=tup+k
print(new_tup)

print(k.count(8))   # count 8 in k
print(k.index(7))   #shows first occurance of 7 in tuple if value is not in tuple then it throws error
print(k.index(4,6,10))  #(value,index,index)
