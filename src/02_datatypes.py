"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE

print("********************* Type Casting String to Num *********************************")

# Write a print statement that combines x + y into the string value 57

print(int(y) + x)

#print(f"hello   {name}")




# YOUR CODE HERE

print("********************* Type Casting Num to String *********************************")

z = ''
z = str(x) + y

print(z)

print("*********************** Type of z using typ() *******************************")

print(f"This is type of z {type(z)}")


print(type(z))