""" 
Insertion Sort
"""

def insertion_sort(A):
    """ sort list of comparable elements into non-decreasing order"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

A = [3, 4, 2, 5, 1, 7]
print(insertion_sort(A))