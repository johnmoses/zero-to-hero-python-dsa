""" 
Radix Sort
This sorts an array by individual digits, starting with the least significant digit (the rightmost one).
"""

# Get unsorted array
arr = [64, 34, 25, 12, 22, 11, 90, 5]

# Create empty array of buckets 0-9 for fitting values
radix_array = [[], [], [], [], [], [], [], [], [], []]

# Get maximum value of array
max_val = max(arr)
exp = 1

# Iterate over array while maximum value is not reached
while max_val // exp > 0:

    while len(arr) > 0:
        val = arr.pop()
        radix_index = (val // exp) % 10
        radix_array[radix_index].append(val)

    for bucket in radix_array:
        while len(bucket) > 0:
            val = bucket.pop()
            arr.append(val)

    exp *= 10

print(arr)