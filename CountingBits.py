# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]


def count_bits(num):
    out = []
    for n in range(num + 1):
        count = 0
        while n > 0:
            n, r = divmod(n, 2)
            count += r
        out.append(count)
    return out


# def count_bits(num):
#     return [str(bin(n)).count('1') for n in range(num + 1)]


# def countBits(self, num: int) -> List[int]:
#     dp = [0] * (num + 1)
#     for i in range(1, num + 1):
#         dp[i] = dp[i // 2] + (i % 2)
#     return dp


print(count_bits(10))

# for i in range(20):
#     print(i & (i-1))
