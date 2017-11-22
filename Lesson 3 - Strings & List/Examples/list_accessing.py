
# Create a new list and fill with 10 numbers.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# This will return the length of the list (number of items)
n = len(my_list)

# This will return the item located at index 5, so its the 6th element.
item = my_list[5]

# Will return a sequence of items, contains every 2nd item from 'my_list'.
sequence_1 = my_list[::2]

# Will return a sequence of items, contains the elemnts betwen index 3 and 8.
sequence_2 = my_list[3:8]

print("The list contains {0} items, an item in the list is {1}".format(n, item))

print("First sequence containing every other item: {0}".format(sequence_1))
print("Second sequence containing items between 3 and 8: {0}".format(sequence_2))
