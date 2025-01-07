"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

Complexity = O(n)
"""

def limit(arr, minimum=None, maximum=None):
    if len(arr) == 0:
        return arr
    if minimum is None:
        minimum = min(arr)
    if maximum is None:
        maaximum = max(arr)
    return list(filter(lambda x: (minimum <= x <= maximum), arr))

arr = [1,2,3,4,5]
minimum = 1
maximum = 3
print(limit(arr, minimum, maximum))