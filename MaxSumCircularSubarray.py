# Given a circular array C of integers represented by A, find the maximum possible sum of a non - empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning of the array.(Formally, C[i] = A[i]
# when 0 <= i < A.length, and C[i + A.length] = C[i] when i >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most once.(Formally, for a subarray C[i],
# C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
# Example 1:
# Input: [1, -2, 3, -2]
# Output: 3
# Explanation: Subarray[3] has maximum sum 3
#
# Example 2:
# Input: [5, -3, 5]
# Output: 10
# Explanation: Subarray[5, 5] has maximum sum 5 + 5 = 10
#
# Example 3:
# Input: [3, -1, 2, -1]
# Output: 4
# Explanation: Subarray[2, -1, 3] has maximum sum 2 + (-1) + 3 = 4
#
# Example 4:
# Input: [3, -2, 2, -3]
# Output: 3
# Explanation: Subarray[3] and [3, -2, 2] both have maximum sum 3
#
# Example 5:
#
# Input: [-2, -3, -1]
# Output: -1
# Explanation: Subarray[-1] has maximum sum - 1
#
# Note:
#     -30000 <= A[i] <= 30000
#     1 <= A.length <= 30000
import sys


def max_subarr_sum(arr):
    subarr_sum = 0
    maxsum = -sys.maxsize
    for num in arr:
        subarr_sum = max(subarr_sum + num, num)
        maxsum = max(maxsum, subarr_sum)
    return maxsum


# def max_subarr_sum_circular(arr):
#     if not arr:
#         return 0
#     if all([e < 0 for e in arr]):  # all values are negative
#         return max(arr)
#
#     maxsum = max_subarr_sum(arr)  # kadane max subarray sum
#     arrsum = 0
#     for i in range(len(arr)):
#         arrsum += arr[i]
#         arr[i] = -arr[i]
#
#     return max(maxsum, arrsum + max_subarr_sum(arr))

# def max_subarr_sum_circular_naive(arr):
#     if not arr:
#         return 0
#     lenarr = len(arr)
#     arr = arr * 2
#
#     maxsum = -sys.maxsize
#     for i in range(lenarr):
#         maxsum = max(maxsum, max_subarr_sum(arr[i:lenarr + i]))
#     return maxsum

def max_subarr_sum_circular(arr):
    if all([e < 0 for e in arr]):  # all values are negative
        return max(arr)
    n = len(arr)

    subarr_sum = 0
    maxsum = -sys.maxsize
    for e in arr:
        subarr_sum = max(e, subarr_sum + e)
        maxsum = max(maxsum, subarr_sum)

    rightsum = arr[-1]
    maxright = [0] * (n - 1) + [arr[-1]]
    for i in range(n - 2, -1, -1):
        rightsum += arr[i]
        maxright[i] = max(rightsum, maxright[i + 1])

    leftsum = 0
    for i in range(n - 2):
        leftsum += arr[i]
        maxsum = max(maxsum, leftsum + maxright[i + 2])
    return maxsum


assert max_subarr_sum_circular([1, -2, 3, -2]) == 3
assert max_subarr_sum_circular([5, -3, 5]) == 10
assert max_subarr_sum_circular([3, -1, 2, -1]) == 4
assert max_subarr_sum_circular([3, -2, 2, -3]) == 3
assert max_subarr_sum_circular([-2, -3, -1]) == -1

# print(max_subarr_sum_circular([1, -2, 3, -4, 5]))
