# library Exercise
class library:
    def __init__(self):
        self.book=[]
        self.book_count=0
    def check(self):
        if(self.book_count==len(self.book)):
            print(f"Program working Correctly and no. of book is {self.book_count}")
        else:
            print("Program not working Properly")

    def add(self,book_name):
        self.book.append(book_name)
        self.book_count+=1

    def show_info(self):
        for book in self.book:
            print(book)    

lib1=library()                            
lib1.add("Hindi")
lib1.add("Hindi")
lib1.add("Hindi")
lib1.add("Hindi")
lib1.check()
lib1.show_info()
# print(lib1.book)