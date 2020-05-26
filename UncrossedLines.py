# We write the integers of A and B (in the order they are given) on two separate horizontal lines.
#
# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
#
#     A[i] == B[j];
#     The line we draw does not intersect any other connecting (non-horizontal) line.
#
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting
# line.
#
# Return the maximum number of connecting lines we can draw in this way.
#
# Example 1:
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[
# 1]=2.
#
# Example 2:
# Input: A = [2, 5, 1, 2, 5], B = [10, 5, 2, 1, 5, 2]
# Output: 3
#
# Example 3:
# Input: A = [1, 3, 7, 1, 7, 5], B = [1, 9, 2, 5, 1]
# Output: 2
#
# Note:
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000


def max_uncrossed_lines(a, b):
    nrows = len(a) + 1
    ncols = len(b) + 1

    dp = [[0] * ncols for _ in range(nrows)]
    for i in range(1, nrows):
        for j in range(1, ncols):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for e in dp:
        print(e)
    return dp[-1][-1]


# def max_uncrossed_lines(a, b):
#     nrows = len(a) + 1
#     ncols = len(b) + 1
#     last_col = 0
#
#     dp = [[0] * ncols for _ in range(nrows)]
#     for i in range(1, nrows):
#         marked_row = False
#         for j in range(1, ncols):
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#             if a[i - 1] == b[j - 1] and j > last_col and not marked_row:
#                 dp[i][j] += 1
#                 last_col = j
#                 marked_row = True
#     for e in dp:
#         print(e)
#     return dp[-1][-1]


a = [1, 4, 2]
b = [1, 2, 4]
assert max_uncrossed_lines(a, b) == 2

a = [2, 5, 1, 2, 5]
b = [10, 5, 2, 1, 5, 2]
assert max_uncrossed_lines(a, b) == 3

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]
assert max_uncrossed_lines(a, b) == 2

a = [2, 1]
b = [1, 2, 1, 3, 3, 2]
assert max_uncrossed_lines(a, b) == 2

a = [1, 1, 3, 5, 3, 3, 5, 5, 1, 1]
b = [2, 3, 2, 1, 3, 5, 3, 2, 2, 1]
print(max_uncrossed_lines(a, b))
