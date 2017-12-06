# Using a 'with' opens the file and sets inside object 'foo'.
with open("multi-lines.txt", "r") as foo:

    # Asignes the contents of the file to the variable 'lines'.
    lines = foo.readlines()

"""
It's important to note here that 'lines' is an array obejct, and each line from
the file is a string object. So each line is placed inside the array at a new
index.

So below where we get the length, we are not getting the length of the file, but
rather the length of the array. The length of an array is number of elements
it contains.
"""

# Gets the number of lines stored within the array.
length = len(lines)

# For each line in the array.
for x in range(length):

    # Print each line.
    print(lines[x])


# We can also select individual lines and print them directly with an index specifier.
print("The first line contains the data: " + lines[0])

