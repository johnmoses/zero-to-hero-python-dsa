"""
Hash Sets
"""
hash_set = [None,'Joy',None,'Lisa',None,'Bob',None,'Mary','Peter',None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
    
def contains(name):
    index = hash_function(name)
    return hash_set[index] == name

print("'Peter' is in the Hash Set:",contains('Peter'))