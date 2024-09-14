# Difference between 'is' and '==' 
# 'is' comapares location of object and '==' compares value

# in python if we create immutable or unchangabe variables and if they hold same value
# then python doesn't waste memory twice

a=5
b=5
print(a is b)
print(a == b)

x="nishant"
y="nishant"
print(x is y)
print(x == y)

l1=[1,2,3,4]  # list is mutable
l2=[1,2,3,4]
print(l1 is l2)
print(l1 == l2)

t1=(1,2,3)   # tuple is immutable
t2=(1,2,3)
print(t1 is t2)
print(t1 == t2)

n1=None
n2=None
print(n1 is n2)
print(n1 == n2)
print(n1 == None)