# Import the pickle module.
import pickle

# Lets create something to be pickled.
picklelist = ["Hello", "World", "This", "Is", "A", "Test!"]

# Now create a file.
file = open('pickle_test.txt', 'wb')

# Now let's pickle picklelist.
pickle.dump(picklelist,file)

# Close the file, and your pickling is complete.
file.close()
