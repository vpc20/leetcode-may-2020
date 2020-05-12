# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
# element which appears exactly once.Find this single element that appears only once.
#
# Example 1:
#
# Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2
#
# Example 2:
#
# Input: [3, 3, 7, 7, 10, 11, 11]
# Output: 10
#
# Note: Your solution should run in O(log n) time and O(1) space.


# def single_non_duplicate(nums):
#     v = 0
#     for n in nums:
#         v ^= n
#     return v


def single_non_duplicate(nums):
    def single(lo, hi):
        if nums[lo - 1] < nums[lo] < nums[lo + 1]:
            return nums[lo]
        if nums[hi - 1] > nums[hi] > nums[hi + 1]:
            return nums[hi]

        if hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]
            else:
                sng1 = single(lo, mid - 1)
                if sng1:
                    return sng1
                sng2 = single(mid + 1, hi)
                if sng2:
                    return sng2

    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[1]:
        return nums[0]
    if nums[-1] > nums[-2]:
        return nums[-1]
    return single(0, len(nums) - 1)


assert single_non_duplicate([1]) == 1
assert single_non_duplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1
assert single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8

assert single_non_duplicate([1, 1, 2]) == 2
assert single_non_duplicate([1, 2, 2]) == 1
assert single_non_duplicate([1, 1, 2, 3, 3]) == 2

assert single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert single_non_duplicate([3, 3, 7, 7, 10, 11, 11]) == 10
