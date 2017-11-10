from mathFunctions import primeNumbers

def main():

    # Capture the prime numbers.
    primes = primeNumbers()

    # For every prime number in the list of primes...
    for i in range(len(primes)):

        # Print each number to the screen.
        print(primes[i])

# Starts the main method.
if __name__ == "__main__":

    main()
