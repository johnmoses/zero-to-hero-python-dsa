""" 
Write a basic example of set data structure
"""

# Create a set of integers
my_set = {1, 2, 3, 4, 5, 5, 5}  # Duplicate values are automatically removed
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Create a set from a list
my_set2 = set([1, 2, 3, 4])  # Convert a list to a set
print(my_set2)  # Output: {1, 2, 3, 4}

# Create an empty set
my_set3 = {}  # This creates an empty dictionary, not an empty set
print(type(my_set3))  # Output: <class 'dict'>

# Create an empty set using the set() constructor
my_set4 = set()  # This creates an empty set
print(type(my_set4))  # Output: <class 'set'>