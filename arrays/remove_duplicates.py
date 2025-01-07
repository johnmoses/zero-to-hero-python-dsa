"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]
Output: [1, 2, 3, 4, 'hey', 'hello']
"""

arr = [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]

def remove_duplicates(arr):
    # Define an array res to store the result
    res = []

    # Iterate over array
    for i in arr:
        if i not in res:
            res.append(i)
    return res

print(remove_duplicates(arr))
