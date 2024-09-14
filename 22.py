# Read line by line
f=open("file_22.txt" , 'r')
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        print(type(line))
        break
    print(line)
    m=line.split(",")
    # print(m)
    print(f"Marks of student {i} in Maths is {m[0]}")
    print(f"Marks of student {i} in Maths is {m[1]}")
    print(f"Marks of student {i} in Maths is {m[2]}")
f.close()
# Readlines
f=open("file_22_a.txt" , 'a')
str=["Line1\n" , "Line2\n" , "Line3\n"]
f.writelines(str)
for i in range(4):
    x=input("Enter string: ")
    f.writelines(x+'\n')
f.close()        
