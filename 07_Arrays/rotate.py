"""
Rotate an array
"""

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify aray in-place
    """
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a
    print(a)

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))