# MAP
def square(x):
    return x*x

l=[1,2,3,4,5]
newlist=[]
# for item in l:
#     newlist.append(square(item))

# map(function,iteratable)
newlist=list(map(square , l))    #we have to typecast it into list because it map return map object
print(l)    
print(newlist)   
newlist=list(map(lambda x:x*x , l))    # we can also pass lambda function
print(l)    
print(newlist)   



# FILTER

# filter(function,iteratable)
ls=[11,12,13,14,15,16]
newls=[]
def cmp(a):
    return a>13

newls=list(filter(cmp , ls))
print(ls)
print(newls)

# REDUCE
# reduce(function,iterable)
from functools import reduce

num=[1,2,3,4,5,6]
# 1+2,3,4,5,6
# 3+3,4,5,6
# 6+4,5,6
# 10+5,6
# 15+6
sum=reduce(lambda x,y:x+y , num)
print(f"Sum of all elements is {sum}")