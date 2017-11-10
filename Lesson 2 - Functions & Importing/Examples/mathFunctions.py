def primeNumbers():

    # Prompt the user to enter a nunber and capture the value.
    numberCap = int(input("Please enter a max range..."))

    # If the user enters a number that is not between 0 and 100, keep asking them
    # until they enter in a valid number.
    while(numberCap > 100 or numberCap <= 0):

        numberCap = int(input("Invalid number, please enter in a new number..."))

    # The empty prime array.
    primeArray = []

    # Now we chack each number within the range specified, passing each  number into
    # another function to do the checking.
    for i in range(numberCap):

       if prime(i):
           primeArray.append(i)

    # Now we have finished all the checking, we can return the list of primes.
    return primeArray


def prime(n):

    # 0 and 1 are not primes.
    if n < 2:
        return False

    # 2 is the only even prime number.
    if n == 2: 
        return True    

    # all other even numbers are not primes.
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers.
    for x in range(3, int(n**0.5) + 1, 2):
        
        if n % x == 0:
            
            return False

    # Number must be prime!
    return True
