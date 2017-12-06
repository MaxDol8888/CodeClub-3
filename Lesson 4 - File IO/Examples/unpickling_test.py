import pickle

# Loads the pickled file.
unpickle_file = open("pickle_test.txt", "rb")

# Unpacks the pickled object into a variable 'variable_'.
variable_ = pickle.load(unpickle_file)

# Closes the pickled file.
unpickle_file.close()

# Prints the now unpickled variable to the console.
print(variable_)
