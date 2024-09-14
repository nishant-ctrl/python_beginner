# seek() and tell()
# f.seek(10)  means jump cursor at 10th character
# f.read(5)   means read 5 from the seeked cursor
# f.tell()  gives current position from where reading is going to start
with open("file23.txt" , 'r') as f:
    f.seek(8)
    print(f"Postion of cursor is {f.tell()}")
    txt=f.read(4)
    print(txt)

# truncate(5)  modify size to "5"
with open("file23_a.txt" , 'w') as f:
    f.write("ABCDEFGHIJKL") 
    f.truncate(6)       