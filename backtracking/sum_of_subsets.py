''' 
Sum of Subsets
'''

def sum_of_subsets(nums: list[int], max_sum: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)
    return result

def create_state_space_tree(
    nums: list[int],
    max_sum: int,
    num_index: int,
    path: list[int],
    result: list[list[int]],
    remaining_nums_sum: int,
) -> None:
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            index + 1,
            [*path, nums[index]],
            result,
            remaining_nums_sum - nums[index],
        )

nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = sum_of_subsets(nums, max_sum)
print(*result)