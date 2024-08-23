#Recurssive function
def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)
    

print(fac(4))
print(fac(5))

def fibonaci(n):
    if n<=1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    
print(fibonaci(5))    
print(fibonaci(10))    
print(fibonaci(4))    
