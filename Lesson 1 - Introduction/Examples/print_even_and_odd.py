limit_ = input("Please set a maximum range: ")

limit_ = int(limit_)

for x in range(limit_):

    # We are currently still lower than the half way point.
    if(x < (limit_ / 2)):

        # Here only show even digits.
        if(x % 2 == 0):

            print(x)
        else:
            continue
    elif(x == 50):

        print("Its 50!!")
        
    # Now we are over the half way point.
    elif(x > (limit_ / 2)):

        # Here only show the odd digits.
        if(x % 2 != 0):

            print(x)

        else:
            continue
        
