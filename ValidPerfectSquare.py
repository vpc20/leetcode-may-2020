# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true
#
# Example 2:
#
# Input: 14
# Output: false
#
import sys


# def digital_root(num):
#     droot = num
#     while droot > 9:
#         droot = sum([int(d) for d in str(droot)])
#     return droot
#
#
# def is_perfect_square(num):
#     if num in [1, 4, 9]:
#         return True
#     if num in [2, 3, 5, 6, 7, 8]:
#         return False
#     if int(str(num)[-1]) in [2, 3, 7, 8]:
#         return False
#     if str(num)[-1] == '0':
#         zero_count = len([d for d in reversed(str(num)) if d == '0'])
#         if zero_count % 2 != 0:
#             return False
#     if str(num)[-1] == '6' and int(str(num)[-2]) % 2 == 0:
#         return False
#     if str(num)[-1] != '6' and int(str(num)[-2]) % 2 != 0:
#         return False
#     if str(num)[-1] == '5' and int(str(num)[-2]) != 2:
#         return False
#     if int(str(num)[-2:]) % 4 != 0 and int(str(num)[-2:]) % 2 == 0:
#         return False
#     return digital_root(num) in [0, 1, 4, 7, 9]


def is_perfect_square(num):
    lo = 0
    hi = num
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid ** 2
        if sq == num:
            return True
        elif sq > num:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def is_perfect_squarex(num):
    for i in range(sys.maxsize):
        if i * i == num:
            return True
        if i * i > num:
            return False


# print(digital_root(24566))
assert is_perfect_square(1) is True
assert is_perfect_square(4) is True
assert is_perfect_square(9) is True
assert is_perfect_square(16) is True
assert is_perfect_square(25) is True
assert is_perfect_square(5776) is True
assert is_perfect_square(2147483647) is False
assert is_perfect_square(681) is False
assert is_perfect_square(801) is False

assert is_perfect_squarex(1) is True
assert is_perfect_squarex(4) is True
assert is_perfect_squarex(9) is True
assert is_perfect_squarex(16) is True
assert is_perfect_squarex(25) is True
assert is_perfect_squarex(5776) is True
assert is_perfect_squarex(2147483647) is False
assert is_perfect_squarex(681) is False
assert is_perfect_squarex(801) is False
