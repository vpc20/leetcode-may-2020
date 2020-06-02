# rod cutting problem
import sys
from itertools import combinations_with_replacement


def max_price_naive(prices, l):
    cut_lengths = list(prices)
    maxp = -sys.maxsize
    for r in range(1, l + 1):
        for comb in combinations_with_replacement(cut_lengths, r):
            if sum(comb) == l:
                maxp = max(maxp, sum([prices[e] for e in comb]))
    return maxp


def max_price(prices, l):
    dp = [0] * (l + 1)
    for currlen in range(1, l + 1):
        maxp = -sys.maxsize
        for pidx in list(prices):
            if pidx <= currlen:
                maxp = max(maxp, prices[pidx] + dp[currlen - pidx])
        dp[currlen] = maxp
    print(dp)
    return dp[-1]


prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10,
          6: 17, 7: 17, 8: 20, 9: 24, 10: 30}

# for l in range(1, 15):
#     assert max_price(prices, l) == max_price_naive(prices, l)

print(max_price(prices, 4))
