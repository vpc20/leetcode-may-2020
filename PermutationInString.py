# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.In other words,
# one of the first string 's permutations is the substring of the second string.
#
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1("ba").
#
# Example 2:
# Input: s1 = "ab" s2 = "eidboaoo"
# Output: False
#
# Note:
#     The input strings only contain lower case letters.
#     The length of both given strings is in range [1, 10,000].
from collections import Counter


def check_inclusion(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
    if lens1 > lens2:
        return False

    s1ctr = Counter(s1)
    s2ctr = Counter(s2[:lens1 - 1])
    for start in range(lens2 - lens1 + 1):
        end = start + lens1 - 1
        s2ctr[s2[end]] += 1
        if s1ctr == s2ctr:
            return True
        s2ctr[s2[start]] -= 1
        if s2ctr[s2[start]] == 0:
            del s2ctr[s2[start]]
    return False


# def check_inclusion(s1, s2):
#     lens1 = len(s1)
#     lens2 = len(s2)
#     s1ctr = Counter(s1)
#     for i in range(lens2 - lens1 + 1):
#         if s1ctr == Counter(s2[i:i + lens1]):
#             return True
#     return False


assert check_inclusion("ab", "eidbaooo") is True
assert check_inclusion("ab", "eidboaoo") is False
assert check_inclusion("adc", "dcda") is True
