"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

arr = [1,2,3,4,5]
minimum = 1
maximum = 3

Complexity = O(n)
"""

def limit1(array, minimum=None, maximum=None):
    if minimum is None and maximum is None:
        return array
    elif minimum is None:
        return [i for i in array if i <= maximum]
    elif maximum is None:
        return [i for i in array if i >= minimum]
    else:
        return [i for i in array if minimum <= i <= maximum]

def limit2(arr, minimum=None, maximum=None):
    if len(arr) == 0:
        return arr
    if minimum is None:
        minimum = min(arr)
    if maximum is None:
        maximum = max(arr)
    return list(filter(lambda x: (minimum <= x <= maximum), arr))

print(limit1([1,2,3,4,5], 1, 3))
print(limit2([1,2,3,4,5], 1, 3))
