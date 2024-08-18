name="Nishant Kumar"  #double quotes
name1='my_program'    #single quotes
print("Hello",name)   #comma leaves a space
print("Hello"+name1)  # + doesnot gives space

apple="He wants to eat an \"apple\""  #use of \" to print quotes
print(apple)
fruit='He wants to eat an "apple"'    #use single quote instead od double quote
print(fruit)

#Multi line string  use '''_''' OR """_"""
str="""Hello World    
How are you
Good"""
print(str)
print("Lets use a for Loop to print all characters\n")
for character in name:             #use for loop to print all characters
    print(character)

#String Slicing
st="Nishant,Ravi"
print(st[0:7])
print(st[:7])    # [0:7]
print(st[2:7])
print(st[:])   # acts like [0:len(name)]
print(st[0:-3])   # acts like [0:len(name)-3]
print(st[-3:-1])   # acts like [len(name)-3:len(name)-1

#String Methods
a="Mango"
print(a.upper())
print(a)   #Strings are immutable i.e. original string not changed
b="APPLE"
print(b.lower())
c="nishant@@@@"
print(c.rstrip("@"))  #only removes last character
d="nishant!!!nishant!!!"
print(d.replace("nishant","jhon"))  #replace all "nishant with "jhon
e="nishant@Kumar@good@programmer"
print(e.split("@"))     #splits at '@'
f="inTroDuction TO pYthoN"
print(f.capitalize())   #keeps capitalize only first letter and rest in small letter
g="Welcome to Python"
print(g.center(20))     #makes the string of 20 size by putting spaces at front
print(len(g.center(20)))     #makes the string of 20 size by putting spaces at front
print(len(g))

print("No. of e in string g",g.count("e"))   #count the repetition
print("No. of nishant in string d is",d.count("nishant"))
strr="Welcome to console !!!"
print(strr.endswith("!!!"))  #check ending
print(strr.endswith("to",6,10))  #check at any index range
print(strr.find("W"))  #return first occurance index
print(strr.find(" "))
print(strr.find("to"))
print(strr.find("z"))   #if not found return -1
print(strr.index(" "))   #if not found gives error else similar to find()
str2="Hihello09877"
str3="Hi hello 09877"
print(str2.isalnum())  #true iff 0-9 A-Z a-z
print(str3.isalnum())
str4="jsgfyuwgfyugwuAHFDYHFYWfgy"
print(str4.isalpha())  #only A-Z a-z
str5="uuug"
print(str5.islower())
# isprintable()
# isspace()
# isupper()
# startswith()
str6="Welcome To Python"
print(str6.istitle())  #true if first letter of each word is capital
str7="HSDvc jscug sghusgyuc UGUCGUWS bsuju"
print(str7.swapcase())
print(str7.title())
