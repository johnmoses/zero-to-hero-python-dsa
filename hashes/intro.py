""" 
Hashes

Write a basic example of hash data structure

Create a set of strings, integers, and mixed data type, and demonstrate the following operations:
    
    Add an item to the set
    Check if an item exists in the set
    Remove an item from the set
    Create a dictionary using { }
    Create a dictionary using dict() constructor
    Access an item
    Access an item using dictionary key
    Access an item using dictionary key and default value

Note: The dictionary key can be any immutable data type (like string, integer, float, tuple, etc.) and the value can be any data type.
"""

# Set of strings
s1 = {"welcome", "To", "Sets"}
print('s1', s1)

#Set of Integers
s2 = {1,2,3,4,5}
print ('s2: ', s2)

#Set of Mixed Data type 
s3 = {"Welcome", "To", "Sets", (1,2,3), 5, 6}
print('s3: ', s3)

s4 = set(("dogs", "cats", "parrots"))
print('s4: ', s4)

s5 = set([1, 2, 3, 3, 4])
print('s5: ', s5)

# Access item
print ("welcome" in s1)

# Remove item
s1.remove ("welcome")
print('Removed first element: ', s1)

# create dictionary using { }
d1 = {1: 'One', 2: 'Two', 3: 'Three'}
print('d1: ', d1)

# create dictionary using dict() constructor
d2 = dict(a = "One", b = "Two", c = "Three")
print('d2: ', d2)
