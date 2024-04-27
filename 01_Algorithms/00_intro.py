"""
Simple Algorithm
"""
def find_max(data):
    max = data[0]
    for val in data:
        if val > max:
            max = val
    return max

data = [1,2,6,4,3,5,8,14,7]
print(find_max(data))