#  Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist,
#  return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
# Note: You may assume the string contain only lowercase letters.
from collections import Counter


def first_uniq_char(s):
    ctr = Counter(s)
    for i, c in enumerate(s):
        if ctr[c] == 1:
            return i
    return -1


def first_uniq_char_one_liner(s):
    return [i for i, c in enumerate(s) if Counter(s)[c] == 1][0] if [i for i, c in enumerate(s) if Counter(s)[c] == 1] else -1


assert first_uniq_char("leetcode") == 0
assert first_uniq_char("loveleetcode") == 2
assert first_uniq_char("dddccdbba") == 8

assert first_uniq_char_one_liner("leetcode") == 0
assert first_uniq_char_one_liner("loveleetcode") == 2
assert first_uniq_char_one_liner("dddccdbba") == 8
