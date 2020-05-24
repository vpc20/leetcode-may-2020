# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
# which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
# IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The
# same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
# Input: "III"
# Output: 3
#
# Example 2:
# Input: "IV"
# Output: 4
#
# Example 3:
# Input: "IX"
# Output: 9
#
# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def roman_to_int(s):
    d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
         'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    intval = 0
    i = 0
    while i < len(s):
        if s[i:i + 2] in d:
            intval += d[s[i:i + 2]]
            i += 2
        else:
            intval += d[s[i]]
            i += 1
    return intval


# d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
#      'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
# for k, v in d.items():
#     print(f"('{k}', {v})")

# romans = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
#           ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

# romans = [('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50),
#           ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), ('CM', 900), ('M', 1000)]
# print(sorted(romans, reverse=True, key=lambda e: e[1]))

assert roman_to_int('I') == 1
assert roman_to_int('II') == 2
assert roman_to_int('III') == 3
assert roman_to_int('IV') == 4
assert roman_to_int('V') == 5
assert roman_to_int('IX') == 9
assert roman_to_int('LVIII') == 58
assert roman_to_int('MCMXCIV') == 1994
