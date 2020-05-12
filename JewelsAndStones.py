# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".
#
# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0
#
# Note:
#     S and J will consist of letters and have length at most 50.
#     The characters in J are distinct.


def num_jewels_in_stones(j, s):
    jset = set(j)
    count = 0
    for e in s:
        if e in jset:
            count += 1
    return count


def num_jewels_in_stones_one_liner(j, s):
    return sum([1 for e in s if e in set(j)])


assert num_jewels_in_stones('aA', 'aAAbbbb') == 3
assert num_jewels_in_stones('z', 'ZZ') == 0

assert num_jewels_in_stones_one_liner('aA', 'aAAbbbb') == 3
assert num_jewels_in_stones_one_liner('z', 'ZZ') == 0
