"""
Merge two Arrays into one
Do not return anything, modify in-place
"""

from typing import List

def merge(arr1: List[int], m: int, arr2: List[int], n: int) -> None:
    for i in range(n):
        arr1[i+m] = arr2[i]

    # Sort list in-place
    arr1.sort()
    print(arr1)

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = 3
merge(arr1, m, arr2, n)