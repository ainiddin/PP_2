#Home,Intro,Get started
print("Hello World!")

# Syntax
#Most commonly amount of indentations is 4 , but it can be from 1 to infinity
#also after first indentation next codes mast be on the same indantat
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
                                            print("Five is greater than two!")

# Comments
"""
You can 
write comments on
a lot of  
lines with this
symbols
"""
print("Hello, World!")
#and with this sign you can write only one line of comment

# Variables
## Variables
x = 5
y = "BATYR"
print(x)
print(y)

## Variable Names
name = "Anton"
na_me = "Anton"
_na_me = "Anton"
naMe = "Anton"
NAME = "Anton"
name2 = "Anton"

## Assign Multiple Values
x = y = z = "coconut"
print(x)
print(y)
print(z)
fruits = ["blueberry", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

## Output Variables
x = 5
y = "John"
print(x, y)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)

## Global Variables
x = "awesome"

def fonction():
  global x
  x = "fantastic"

fonction()

print("Python is " + x)

# Data Types
x = 5
print(type(x))

# Numbers
x = 1
y = 2.8
z = 1j
w = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print(type(w))

# Casting
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

## Slicing Strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

## Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
a = " Hello, World! "
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

## String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

## Format - Strings
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

## Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)







