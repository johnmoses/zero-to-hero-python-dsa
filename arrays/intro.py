"""
Array
Let's find the minimum value of an array
"""
# Define the array
array = [6, 13, 9, 3, 11, 19]

# Initialize 'min_val' variable
min_val = array[0]

# Iterate over the array
for i in array:
    if i < min_val:
        min_val = i
        
print('Minimum value: ',min_val) # Step 4