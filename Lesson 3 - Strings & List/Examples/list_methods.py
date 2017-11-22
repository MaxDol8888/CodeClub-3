# Lets create a new list
L = ['hello','world','this','is','a','test','hello', 'world']

print("'world' appears: {0} times in list L".format(L.count('world')))

print("The lowest occurrence of the word 'world' is at index {0}".format(L.index('world')))

# We can add a new item to the list:
L.insert(3, 'Python')

print(L)

# Now lets reverse the list
L.reverse()

print("The list reversed: {0}".format(L))
