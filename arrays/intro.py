"""
Simple Arrays and operations
"""
from array import *

# Empty
arr0 = []

# Simple
arr1 = ['a', 'b', 'c', 'd', 'e']
arr2 = array('i',[1,2,3,4,5])
arr3 = [1, 2, 3, 4, 5]

#Mixed types
arr4 = ['1', '2', 'three', '1.5']

# Nested
arr5 = ['James', ['Dev', 'Manager']]
arr6 = [
    ['Carrot','Peper','Okro'], 
    ['Orange','Mango','Water mellon'], 
    ['Stove','Cooker','Refrigerator']
]

print(arr0)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)

# Iterating over items
print('Iterate')
for i in arr1:
    print(i)

# Access individual elements
print('Access: ', arr1[3])

# Append value
arr1.append('f')
print('Append: ', arr1)

# Insert value
arr1.insert(3,'g')
print('Remove: ', arr1)

# Extend
arr1.extend(arr2)
print('Extend:', arr1)

# Add from another list
tempList = [21,22,23]
arr2.fromlist(tempList)
print('Add:', arr2)

# Remove element
arr3.remove(2)
print('Remove:', arr3)

# Remove last element
arr4.pop()
print('Pop: ', arr4)

# Fetch element
print('Fetch: ', arr3.index(5))

# Reverse array
arr5.reverse()
print('Reverse: ', arr5)

# Reverse back
arr5.reverse()
print('Reverse back:', arr5)