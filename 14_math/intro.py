"""
Two sum
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    low, high = 0, len(nums) -1
    while low < high:
        num = nums[low] + nums[high]
        if num == target:
            return (low+1, high+1)
        elif num < target:
            low += 1
        else:
            high -= 1
    return [-1, -1]

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))