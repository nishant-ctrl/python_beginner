# File Handling

f=open("file1.txt" , 'r')   # default is read mode
txt=f.read()
print(txt)
f.close()
f=open("file2.txt" , 'w')   # if a file doesn,t exist and we open in write mode it automatically creates it
f.write("Written through python program.")
f.close()
f=open("file2.txt" , 'a')
f.write("Appended text.")
f.close()

# This is quite boring . we have to close file. 
# Another way is

with open("file2.txt" , 'a') as f:
    f.write("Written through with syntax")


