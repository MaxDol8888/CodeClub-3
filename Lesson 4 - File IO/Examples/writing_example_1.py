foo = open("writeme.txt", "w")

foo.write("Python is a great programming language!!")

Fname = foo.name

foo.close()

print("Finished writing string to file: " + Fname)
