# A function we have created to print a sentance.
def helloWorld():

    print("Hello, World! I am being called from inside a function!")

# The modules main function.
def main():

    print("This is being called from the main function method.")
    
    helloWorld()

# Start of the module (calls the main function).
if __name__ == "__main__":

    main()
