def addNumbers(a, b):

    return (a, b, a + b)

def main():

    number1 = int(input("Please enter the first numer..."))
    number2 = int(input("Please enter the second number..."))

    result = addNumbers(number1, number2)

    print("The result of adding {0} and {1} is {2}".format(result[0], result[1], result[2]))

if __name__ == "__main__":

    main()
