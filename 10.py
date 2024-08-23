letter="My name is {} and I am from {}.I am {} years old."
name="Nishant Kumar"
place="Patna"
age=19.759729
letter=letter.format(name,place,age)
# letter=letter.format("Nishant","Bihar",19)
print(letter)

letter1="My name is {1} and I am from {2}.I am {0} years old."    #older way
print(letter.format(age,name,place))

#using fstrings
print(f"My name is {name} and I am from {place}.I am {age} years old.")
print(f"My name is {name} and I am from {place}.I am {age:.2f} years old.")
print(f"My name is {{name}} and I am from {{place}}.I am {{age}} years old.")  #to print as it is