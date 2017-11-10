# This importes only the function 'helloWorld'
from functions import helloWorld

print("Here we are importing only a function from the a module.")

# Create a variable and store the imported function.
func = helloWorld

# Variable acts like a function, so call like a function.
func()

# We can also call the imported function directly.
helloWorld()
