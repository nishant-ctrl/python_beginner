a=[5,1,7,2,8,11]
print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b=[4,1,0,8,9,7,0,-1,0]
print(b)
b.reverse()
print(b)
print(b.index(7))
print(b.count(0))

#copying a list
c=[4,1,0,8,9,7,0,-1,0]
l=c   #if we change c then l will also be changed i.e. l is reference to c
l=c.copy()  #makes copy of c and stores in l
h=c+a   #adds c and a and stores in h
print(h)
c.extend(a)    #add a at last of c
print(c)