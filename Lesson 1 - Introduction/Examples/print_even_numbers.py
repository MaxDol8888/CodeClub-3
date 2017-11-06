# Take in input from the user.
range_ = input("Please enter in an upper range: ")

# Convert the input into an integer type.
range_ = int(range_)

# Start the for-loop.
for i in range(range_):

    # now we can check if the number is odd or even.
    if((i % 2) == 0):

        # We know this number is even, so print.
        print(i)
    else:
        # This must therefore be odd, so ignore.
        continue


