foo = open("readme.txt", "r")

print("The file name is: " + foo.name)
print("Opening file with mode: " + foo.mode)
print("Is file closed? " + str(foo.closed))

print("Contents: " + foo.read())
foo.close()
