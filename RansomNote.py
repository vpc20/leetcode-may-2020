# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a
# function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will
# return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
from collections import Counter


def can_construct(ransom_note, magazine):
    ctr = Counter(magazine)
    for c in ransom_note:
        if c in ctr:
            if ctr[c] == 0:
                return False
            else:
                ctr[c] -= 1
        else:
            return False
    return True


assert can_construct("a", "b") is False
assert can_construct("aa", "ab") is False
assert can_construct("aa", "aab") is True


