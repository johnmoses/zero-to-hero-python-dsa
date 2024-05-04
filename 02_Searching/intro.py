"""
Search Algorithms
"""

def indexOfMin(data):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(data):
        if data[currentIndex] < data[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

data = [1,2,3]
print('Minimum index...', indexOfMin(data))