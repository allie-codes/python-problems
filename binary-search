# numbers = [-5, 0, 3, 6, 10, 15, 20]
# target = 6

# Your function should return: 3


def binary_search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        midpoint = int((i + j) / 2)
        if nums[midpoint] == target:
            return midpoint
        elif target < nums[midpoint]:
            j = midpoint - 1
        elif target > nums[midpoint]:
            i = midpoint + 1

    return -1


print(binary_search([-5, 0, 3, 6, 10, 15, 20], 6))
