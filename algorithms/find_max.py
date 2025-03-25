""" 
Find maximum number from array of numbers
Input data:
    data = [1,2,6,4,3,5,8,14,7]
Output: 14
"""
def findMax(data):
    max = data[0]
    for d in data:
        if d > max:
            max = d
    return max

print(findMax([1,2,6,4,3,5,8,14,7]))