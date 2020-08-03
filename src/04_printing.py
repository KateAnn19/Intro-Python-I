"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

myTuple = (x,y,x)

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

format = "x is %s, y is %s,  z is %s!"

print(format % myTuple)

# Use the 'format' string method to print the same thing


txt = "X is {0}, y is {1}, z is {2}"
txt2 = "X is {num1}, y is {num2}, z is {num3}".format(num1 = 20, num2= 30, num3="hello there")
txt3 = "X is {}, y is {}, z is {}".format(1,2,"howdy!")
print(txt.format(10, 2.23552, "I like turtles!"))
print(txt2)
print(txt3)



# Finally, print the same thing using an f-string