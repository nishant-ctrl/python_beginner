marks=[10,12,33,42,99,73,67,87,1]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==4):
#         print("Awesome")
#     index+=1

# enumerate function returns a tuple(index,value)
#then the first_value->>index and second_value->>value
for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print("Awesome")
print("\n")    
# by default index starts from 0
# But we can also specify starting index
for index,mark in enumerate(marks , start=2):
    print(mark)
    if(index==4):
        print("Awesome")
            