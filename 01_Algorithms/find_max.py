""" 
Find maximum number from array of numbers
"""
def find_max(data):
    max = data[0]
    for val in data:
        if val > max:
            max = val
    return max

listData = [1,2,6,4,3,5,8,14,7]
print(find_max(listData))