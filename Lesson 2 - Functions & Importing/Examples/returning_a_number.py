# Function that takes two numbers and returns the result.
def addNumbers(a, b):

    """
    This function could also look like: 'return a + b'.
    """
    total = a + b

    return total

# The main function, calls the adDNumbers function.
def main():

    # Capture user input and convert to integers.
    number1 = int(input("Please enter the first number..."))
    number2 = int(input("Please enter the second number..."))

    # Capture the result of the function.
    total = addNumbers(number1, number2)

    print("The total of {0} and {1} is {2}".format(number1, number2, total))

# Calls the main function.
if __name__ == "__main__":

    main()
    
