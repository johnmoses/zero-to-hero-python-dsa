# Find maximum number

def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

if __name__ == "__main__":
    numbers = [2, 4, 5, 6, 9, 34, 20, 2]
    print(f"Min is {find_min(numbers)}")