# Take input form the user and store them in two different variables.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the data type of the two variables from str to int.
num1 = int(num1)
num2 = int(num2)

# Add the two ints together.
sum_ = num1 + num2

# Print the results to the screen, using the format function.
print ("The sum of {0} and {1} is {2}".format(num1,num2, sum_))




