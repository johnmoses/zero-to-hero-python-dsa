"""
Array
Write a basic array function
to find the minimum value in a given array.

Step 1: Define the array
Step 2: Initialize a variable to store the minimum value
Step 3: Iterate over the array and check each element
Step 4: Compare each element with the current minimum value
Step 5: Update the minimum value if a smaller element is found
Step 6: Return the minimum value

Example usage:
    array = [6, 13, 9, 3, 11, 19]
"""

# Define or create the array
array = [6, 13, 9, 3, 11, 19]

# Initialize 'min_val' variable to element at position 0 (zero)
min_val = array[0]

# Iterate over the array and check each element
for i in array:
    if i < min_val:
        min_val = i
        
print('Minimum value: ',min_val) # Step 4