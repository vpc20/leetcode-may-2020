# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra
# space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


# def find_disappeared_numbers(nums):
#     if not nums:
#         return []
#     n = len(nums)
#     allset = set(range(1, n + 1))
#     nset = set(nums)
#     if allset == nset:
#         return []
#
#     out = [i for i in range(1, n + 1) if i not in nset]
#     return out


# def find_disappeared_numbers(nums):
#     allset = set(range(1, len(nums) + 1))
#     return list(allset.difference(set(nums)))


# def find_disappeared_numbers(nums):
#     allset = set(range(1, len(nums) + 1))
# return list(allset - set(nums))


def find_disappeared_numbers(nums):
    nset = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in nset]


print(find_disappeared_numbers([]))
print(find_disappeared_numbers([1, 2]))
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
