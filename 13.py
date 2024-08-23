# sets in python
# set is a collection of well defined objects
# repetition of value is not allowed in set like in maths

s={1,2,3,1,5,6,2,2,1}
print(s)
# sets are un-changable
# order is not maintained
info={"Carrot" , 10 , True , 10 , 2.3 , 2.3}
print(info)

hom={}
print(type(hom))  # showing type dictionary
hom=set()  # use this to create empty set
print(type(hom))

for data in info:
    print(data)


#SETS operations
a={1,2,5,6}
b={2,3,4,7,8}
print(a.union(b))  # a and b is not updated
print(a,b)        
# to update a as aUb
a.update(b)
print(a)


c={1,2,5,6}
d={2,3,4,7,8}
g=c.intersection(d)   # c and d is not updated
print(g)  
print(c,d)        
# to update d as d intersecton c
d.intersection_update(c)
print(d)


# Symmetric Difference
# (a union b) - (a intersection b)
#  this gives a set that is not not common in a and b
print(c.symmetric_difference(d))
c.difference_update(d)
print(c)

x={1,2,3}
y={2,3,4,5}
print(x.difference(y))   # value which is in x but not in y   i.e.  x-y


# disjoint set =>  a intersection b is phi or empty
q={1,2}
w={3,4}
print(q.isdisjoint(w))
e={1,2,3,4,5}
f={2,3}
print(e.issuperset(f))
print(f.issuperset(e))
print(e.issubset(f))
print(f.issubset(e))

n={2,3,4,7,8}
n.remove(2)
print(n)
# n.remove(10)  # throws error if value is not present in set
n.discard(10)
print(n)


# pop a set
# removes randon value and show
b={1,2,3,4,5,6,7}
temp=b.pop()
print(b)
print(temp)

# deleting a set
# del b
# print(b)  throws error as b is deleted
b.clear()
print(b)

if 1 in e:
    print("Yes")
else:
    print("NO")
