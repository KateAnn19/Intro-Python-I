# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print("********* Append ********")
x.append(4)

print(x)

print("********* Join two lists ********")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

x = x + y

# for l in y:
#   x.append(y)


#x.extend(y)
print(x)

print("********* Delete from list at index ********")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
del x[4]
#x.remove(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print("********* Add to List at Specific Index ********")
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print("********* Print Length of List ********")

print(f"The length of x is :  {len(x)} ")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE