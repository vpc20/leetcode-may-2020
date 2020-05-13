# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is
# the smallest possible.
#
# Note:
#     The length of num is less than 10002 and will be ≥ k.
#     The given num does not contain any leading zero.
#
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#
# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
#
# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
from itertools import combinations


def remove_kdigits_brute(num, k):
    if k >= len(num):
        return '0'

    minval = '9' * 10001
    for comb in combinations(range(len(num)), k):
        newval = ''.join([n for i, n in enumerate(num) if i not in comb])
        minval = min(minval, newval)
    x = minval.lstrip('0')
    return x if x else '0'


def remove_kdigits(num, k):
    if k >= len(num):
        return '0'

    numlist = list(num)
    i = 0
    while i < len(numlist) - 1 and k != 0:
        if numlist[i] > numlist[i + 1]:
            numlist.pop(i)
            k -= 1
            if i > 0:
                i -= 1
            continue
        i += 1

    for i in range(k):
        numlist.pop()
    newval = ''.join(numlist).lstrip('0')
    return newval if newval else '0'


# def remove_kdigits(num, k):
#     if k >= len(num):
#         return '0'
#
#     pop_idx = []
#     for i in range(len(num) - 1):
#         if num[i] > num[i + 1]:
#             pop_idx.append(i)
#             k -= 1
#             if k == 0:
#                 break
#     new_arr = [n for i, n in enumerate(num) if i not in pop_idx]
#     for i in range(k):
#         new_arr.pop()
#     newval = ''.join(new_arr).lstrip('0')
#     return newval if newval else '0'


# assert remove_kdigits_brute('1432219', 3) == '1219'
# assert remove_kdigits_brute('10200', 1) == '200'
# assert remove_kdigits_brute('10', 2) == '0'
# assert remove_kdigits_brute('10', 1) == '0'

assert remove_kdigits('1432219', 3) == '1219'
assert remove_kdigits('10200', 1) == '200'
assert remove_kdigits('10', 2) == '0'
assert remove_kdigits('10', 1) == '0'
assert remove_kdigits('112', 1) == '11'
assert remove_kdigits('5337', 2) == '33'
assert remove_kdigits('1234567890', 9) == '0'

for n in range(100000):
    for k in range(1, len(str(n)) + 1):
        print(n, k)
        # print(remove_kdigits_brute(str(n), k))
        # print(remove_kdigits(str(n), k))
        assert remove_kdigits_brute(str(n), k) == remove_kdigits(str(n), k)

# print(remove_kdigits_brute('1100', 2))
# print(remove_kdigits('1100', 2))

