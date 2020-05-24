# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
# Input: "tree"
# Output: "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#
# Example 2:
# Input: "cccaaa"
# Output: "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
# Example 3:
# Input: "Aabb"
# Output: "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# def frequency_sort(s):
#     return ''.join(sorted(s, reverse=True, key=lambda e: (s.count(e), e)))
import heapq
from collections import Counter


# def frequency_sort(s):
#     sctr = Counter(s)
#     ctup = [(c, sctr[c]) for c in s]
#     return ''.join([c for c, _ in sorted(ctup, reverse=True, key=lambda e: (e[1], e[0]))])

# def frequency_sort(s):
#     sctr = Counter(s)
#     return ''.join([c * count for c, count in sorted(sctr.items(), reverse=True, key=lambda e: (e[1], e[0]))])

def frequency_sort(s):
    sctr = Counter(s)
    sorted_ch = sorted(sctr.items(), reverse=True, key=lambda e: (e[1], e[0]))
    return ''.join([c * count for c, count in sorted_ch])


def frequency_sort1(s):
    ctr = Counter(s)
    res = ''
    hq = []
    for char, freq in ctr.items():
        heapq.heappush(hq, (-freq, char))

    while hq:
        freq, char = heapq.heappop(hq)
        res += -freq * char

    return res


assert frequency_sort("tree") == "eetr"
assert frequency_sort("cccaaa") == "cccaaa"
assert frequency_sort("Aabb") == "bbaA"
assert frequency_sort("loveleetcode") == "eeeeoollvtdc"
