"""
Two Sum
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""

def two_sum(nums, target):
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

def two_sum_2(nums, target):
    # Define a dictionary
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return dic[num], i 
        else:
            dic[target - num] = i
    return None

print(two_sum_2(nums, target))