# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.
#
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
from itertools import combinations


def three_sum_naive(nums):
    out = []
    for comb in combinations(nums, 3):
        if sum(comb) == 0:
            x = sorted(list(comb))
            if x not in out:
                out.append(x)
    # if not out:
    #     return []
    # sout = sorted(out)
    # result = [sout[0]]
    # for i in range(1, len(sout)):
    #     if sout[i] != sout[i - 1]:
    #         result.append(sout[i])
    # return result
    return out


def three_sum(nums):
    pass


print(three_sum_naive([-1, 0, 1, 2, -1, -4]))
