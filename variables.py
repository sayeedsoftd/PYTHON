"""This is a comment
written in
more than just one line
"""
print("Hello, World!")
x = 5
y = "John"
print(type(x)) #use type function (int)
print(type(y))#use type function (string)
x = 4       # x is of type int
#x = "Sally" # x is now of type str
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x+y+z)
# golbal variable 
x = "omg"

def myfunc():
  print("Python is " + x)

myfunc()

x = "some"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)