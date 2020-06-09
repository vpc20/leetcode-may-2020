# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Note:
# You may assume that you have an infinite number of each kind of coin.

import sys


# def coin_change(coins, amount):
#     dp = [0] * (amount + 1)
#     for curr_amt in range(1, amount + 1):
#         minval = amount
#         for coin in coins:
#             if coin <= curr_amt:
#                 minval = min(minval, 1 + dp[curr_amt - coin])
#                 dp[curr_amt] = minval
#     print(dp)
#     return dp[-1]


def coin_change(coins, amount):
    dp = [0] * (amount + 1)
    for curr_amt in range(1, amount + 1):
        minval = sys.maxsize
        for coin in coins:
            if coin <= curr_amt:
                if dp[curr_amt - coin] != -1:
                    minval = min(minval, 1 + dp[curr_amt - coin])
        dp[curr_amt] = minval if minval != sys.maxsize else -1
    return dp[-1]


def coin_change_recur(coins, amount):
    def coin_change_x(amt, count):
        # print(f'coin_change_x({amt}, {count})')
        nonlocal minval
        if amt == 0:
            minval = min(minval, count)
        else:
            for coin in coins:
                if coin <= amt:
                    coin_change_x(amt - coin, count + 1)

    minval = sys.maxsize
    coins.sort()
    coin_change_x(amount, 0)
    return minval if minval != sys.maxsize else -1


# print(coin_change([1, 2, 5], 11))  # 3
# print(coin_change_recur([1, 2, 5], 11))  # 3

# print(coin_change([2], 3))  # -1
# print(coin_change_recur([2], 3))  # -1

coins = [1, 5, 10, 25, 50]
for i in range(40):
    assert coin_change(coins, i) == coin_change_recur(coins, i)
