# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
# value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


# def search_range(nums, target):
#     try:
#         first = nums.index(target)
#     except ValueError:
#         return [-1, -1]
#
#     nums.reverse()
#     last = len(nums) - 1 - nums.index(target)
#     return [first, last]


def search_range(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target <= nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    if 0 <= lo < len(nums) and nums[lo] == target:
        first = lo
    else:
        return [-1, -1]

    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    last = hi

    return [first, last]


def first_occurence(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target <= nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo if 0 <= lo < len(nums) and nums[lo] == target else -1


def last_occurence(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi if 0 <= hi < len(nums) and nums[hi] == target else -1


assert first_occurence([1], 2) == -1
assert first_occurence([2], 2) == 0
assert first_occurence([1, 2], 2) == 1
assert first_occurence([2, 3], 2) == 0
assert first_occurence([1, 2, 3], 2) == 1
assert first_occurence([1, 2, 2, 3], 2) == 1
assert first_occurence([1, 1, 2, 3], 2) == 2
assert first_occurence([1, 1, 2, 3, 4], 2) == 2

assert last_occurence([1], 2) == -1
assert last_occurence([2], 2) == 0
assert last_occurence([1, 2], 2) == 1
assert last_occurence([2, 3], 2) == 0
assert last_occurence([1, 2, 3], 2) == 1
assert last_occurence([1, 2, 2, 3], 2) == 2
assert last_occurence([1, 1, 2, 3], 2) == 2
assert last_occurence([1, 1, 2, 3, 4], 2) == 2

assert search_range([1, 1, 2, 3, 4], 5) == [-1, -1]
assert search_range([1, 1, 2, 3, 4], 2) == [2, 2]
assert search_range([1, 1, 2, 2, 3, 4], 2) == [2, 3]
assert search_range([1, 1, 1, 2, 2, 3, 4], 2) == [3, 4]
