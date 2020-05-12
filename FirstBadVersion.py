# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
# ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
# find the first bad version. You should minimize the number of calls to the API.
#
# Example:
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    arr = [False, False, False, True, True]
    # arr = [False, True, True, True, True]
    # arr = [False, False, True, True, True]
    return arr[version - 1]


def first_bad_version(n):
    lo = 0
    hi = n - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if isBadVersion(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


# def first_bad_version(n):
#     lo = 0
#     hi = n - 1
#     mid = (lo + hi) // 2
#
#     while lo <= hi:
#         if isBadVersion(mid + 1):
#             if not isBadVersion(mid):
#                 return mid + 1
#             else:
#                 hi = mid
#         else:
#             if isBadVersion(mid + 2):
#                 return mid + 2
#             else:
#                 lo = mid
#         mid = (lo + hi) // 2
#     return -1

def first_true(arr):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


print(first_bad_version(5))
