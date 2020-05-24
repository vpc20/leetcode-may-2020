# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The
# intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a
# closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]]
#        B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
#
# Note:
#     0 <= A.length < 1000
#     0 <= B.length < 1000
#     0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9


def interval_intersection(a, b):
    intersections = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            intersections.append([lo, hi])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return intersections

# incorrect
# def interval_intersection(a, b):
#     if a == [] or b == []:
#         return []
#     intersections = []
#
#     i = j = start = end = 0
#     while i < len(a) and j < len(b):
#         if a[i][0] > b[j][1] or b[j][0] > a[i][1]:
#             continue
#         else:
#             if b[j][0] <= a[i][0] <= b[j][1]:
#                 start = a[i][0]
#             if a[i][0] <= b[j][0] <= a[i][1]:
#                 start = b[j][0]
#
#             if b[j][0] <= a[i][1] <= b[j][1]:
#                 end = a[i][1]
#             if a[i][0] <= b[j][1] <= a[i][1]:
#                 end = b[j][1]
#             intersections.append([start, end])
#             print(intersections)
#
#         if a[i][1] < b[j][1]:
#             i += 1
#         else:
#             j += 1
#     return intersections


# incorrect
# def interval_intersection(a, b):
#     ab = sorted(a + b)
#     print(ab)
#     intersections = []
#     for i in range(1, len(ab)):
#         if ab[i][0] > ab[i - 1][1]:
#             continue
#         intersections.append([ab[i][0], ab[i - 1][1]])
#     return intersections


# a = [[0, 2], [5, 10], [13, 23], [24, 25]]
# b = [[1, 5], [8, 12], [15, 24], [25, 26]]
# print(interval_intersection(a, b))

# a = [[3, 5], [9, 20]]
# b = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
# print(interval_intersection(a, b))
# Input:  [[3,5],[9,20]]
#         [[4,5],[7,10],[11,12],[14,15],[16,20]]
# Output: [[4,5],[9,10],[11,12],[14,15],[16,20]]
#
# 0                                       1                                       2
# 0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0
#             |-------|               |-------------------------------------------|
#                 |---|       |-----------|   |---|       |---|   |---------------|

# a = [[4, 11]]
# b = [[1, 2], [8, 11], [12, 13], [14, 15], [17, 19]]
# assert interval_intersection(a, b) == [[8, 11]]

a = [[0, 2], [5, 10], [13, 23], [24, 25]]
b = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(interval_intersection(a, b))
