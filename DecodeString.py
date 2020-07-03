# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# from functools import lru_cache
from string import ascii_uppercase


# @lru_cache(maxsize=99999)
def decode_str(s):
    def decode(s, res):
        if s == '':
            strs.append(res)
            return

        i = int(s[0]) - 1
        if 0 <= i <= 8:
            decode(s[1:], res + ascii_uppercase[i])

        i = int(s[:2]) - 1
        if len(s) >= 2 and 9 <= i <= 25:
            decode(s[2:], res + ascii_uppercase[i])

    strs = []
    decode(s, '')
    return strs


def decode_str_dyna(s):
    if not s:
        return ''
    n = len(s)
    dp = [[] for _ in range(n + 1)]

    dp[0].append('')
    x = '' if s[0] == "0" else ascii_uppercase[int(s[0]) - 1]
    dp[1].append(x)

    for i in range(2, n + 1):
        j = int(s[i - 1])
        if j > 0:
            for e in dp[i - 1]:
                dp[i].append(e + ascii_uppercase[j - 1])

        j = int(s[i - 2:i])
        if 10 <= j <= 26:
            for e in dp[i - 2]:
                dp[i].append(e + ascii_uppercase[j - 1])

    return dp[-1]


# print(num_decodings('0'))
# print(num_decodings('20'))
# print(num_decodings('260'))
# print(num_decodings('1'))
# print(num_decodings('12'))
# print(num_decodings(''))
# print(num_decodings('2'))
# print(num_decodings('22'))
# print(num_decodings('226'))
# print(num_decodings('026'))
# print('')
# print(num_decodings_dyna(''))
# print(num_decodings_dyna('2'))
# print(num_decodings_dyna('22'))
# print(num_decodings_dyna('026'))

# print(num_decodings_dyna('10'))
# print(num_decodings_dyna(''))
# print(ascii_lowercase[0])

# decode_str('226')
# print(decode_str('1'))
# print(decode_str('2'))
# print(decode_str('3'))
# print(decode_str('4'))
# print(decode_str('5'))
# print(decode_str('6'))
# print(decode_str('7'))
# print(decode_str('8'))
# print(decode_str('9'))
# print(decode_str('10'))
# print(decode_str('11'))
# print(decode_str('12'))
# print(decode_str('026'))
# print(decode_str('1126'))

# print(decode_str('2'))
# print(decode_str('22'))
# print(decode_str('226'))

print(decode_str('226'))
print(decode_str_dyna('226'))
