# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary
# representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
# So you need to output 2.

# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0.
# So you need to output 0.

# Note:
#     The given integer is guaranteed to fit within the range of a 32-bit signed integer.
#     You could assume no leading zero bit in the integer’s binary representation.


# def find_complement(num):
#     return int(''.join(['0' if c == '1' else '1' for c in (bin(num)[2:])]), 2)

def find_complement(num):
    b = bin(num)[2:]
    y = ''.join(['0' if c == '1' else '1' for c in b])
    return int(y, 2)


def find_complement_one_liner(num):
    return int(''.join(['0' if c == '1' else '1' for c in (bin(num)[2:])]), 2)


assert find_complement(5) == 2
assert find_complement(1) == 0

assert find_complement_one_liner(5) == 2
assert find_complement_one_liner(1) == 0
