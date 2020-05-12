# Given an array of size n, find the majority element. The majority element is the element that appears more than
# ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
# Input: [3,2,3]
# Output: 3
#
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2
from collections import defaultdict, Counter


def majority_element(nums):
    ctr = defaultdict(int)
    target = len(nums) // 2
    for n in nums:
        if n in ctr:
            if ctr[n] == target:
                return n
            else:
                ctr[n] += 1
        else:
            ctr[n] = 1
    return n


def majority_elementx(nums):
    ctr = Counter(nums)
    tgt = len(nums) // 2
    for k, v in ctr.items():
        if v > tgt:
            return k


def majority_element_one_liner(nums):
    return sorted(nums, key=lambda e: nums.count(e))[-1]


assert majority_element([3, 2, 3]) == 3
assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
assert majority_element([1]) == 1

assert majority_elementx([3, 2, 3]) == 3
assert majority_elementx([2, 2, 1, 1, 1, 2, 2]) == 2
assert majority_elementx([1]) == 1

assert majority_element_one_liner([3, 2, 3]) == 3
assert majority_element_one_liner([2, 2, 1, 1, 1, 2, 2]) == 2
assert majority_element_one_liner([1]) == 1
