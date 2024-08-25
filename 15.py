#Exception Handling

a=(input("Enter the number: "))
print(f"Multiplication Table of {a}")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*int(i)}")
except Exception as e:                                     # error message is stored in e
    print(e)                                               # we cant print anything 
    print("Custom Message")



# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*int(i)}")
# except:
#     print("Custom Message")    

print("Important codes")    

try:
    x=int(input("Enter number: "))
    a=[0,1,2,3,4]
    print(a[x])
except ValueError:
    print("Entered number is not integer")
except IndexError:
    print("Index is not correct")    


# finnaly clause
# the content of finally is always executed whether error occured or not

try:
    lst=[0,1,2,3,4]
    i=int(input("Enter index: "))
    print(lst[i])
except:
    print("ERROR OCCURED")
finally:
    print("This code always ececuted")

# useful in function
def fun1(): 
    try:
        lst=[0,1,2,3,4]
        i=int(input("Enter index: "))
        print(lst[i])
        return 1
    except:
        print("ERROR OCCURED")
        return 0
    finally:
        print("This code always ececuted")  

c=fun1()
print(c)                     