# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#


def permute(nums):
    def permutation(nums):
        if len(nums) == 1:
            yield [nums[0]]
            return
        for i, e in enumerate(nums):
            for p in permutation(nums[:i] + nums[i + 1:]):
                yield [e] + p

    return list(permutation(nums))


print(permute([1]))
print(permute([1, 2, 3]))
