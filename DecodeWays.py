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
from functools import lru_cache


@lru_cache(maxsize=99999)
def num_decodings(s):
    if s == '':
        return 1
    ctr = 0

    if 1 <= int(s[0]) <= 9:
        ctr = num_decodings(s[1:])
    if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
        ctr += num_decodings(s[2:])

    return ctr


def num_decodings_dyna(s):
    if not s:
        return 1
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, n + 1):
        if int(s[i - 1]) > 0:
            dp[i] = dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[-1]


assert num_decodings('') == 1
assert num_decodings('0') == 0
assert num_decodings('05') == 0
assert num_decodings('40') == 0
assert num_decodings('10') == 1
assert num_decodings('12') == 2
assert num_decodings('2') == 1
assert num_decodings('22') == 2
assert num_decodings('226') == 3

assert num_decodings_dyna('') == 1
assert num_decodings_dyna('0') == 0
assert num_decodings_dyna('05') == 0
assert num_decodings_dyna('40') == 0
assert num_decodings_dyna('10') == 1
assert num_decodings_dyna('12') == 2
assert num_decodings_dyna('2') == 1
assert num_decodings_dyna('22') == 2
assert num_decodings_dyna('226') == 3

