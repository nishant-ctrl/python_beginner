import os
print(os.getcwd())

list=os.listdir("os_module/")
print(list)

# def ren()

i=0
for file in list:
    i+=1
    os.rename(f"os_module/{file}", f"os_module/{i}.png")


# os.mkdir("os_module/b.png")
list=os.listdir("os_module/")
print(list)