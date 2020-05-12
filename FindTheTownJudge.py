# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the
# town judge.
#
# If the town judge exists, then:
#
#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person
# labelled b.
#
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#
# Example 1:
# Input: N = 2, trust = [[1,2]]
# Output: 2
#
# Example 2:
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
#
# Example 3:
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
# Example 4:
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
#
# Example 5:
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
#
# Note:
#
#     1 <= N <= 1000
#     trust.length <= 10000
#     trust[i] are all different
#     trust[i][0] != trust[i][1]
#     1 <= trust[i][0], trust[i][1] <= N


# def find_judge(n, trust):
#     pset = set(range(1, n + 1))
#     for f, s in trust:
#         if f in pset:
#             pset.remove(f)
#     if len(pset) != 1:
#         return -1
#     judge = list(pset)[0]
#
#     pair_set = set()
#     for i in range(1, n + 1):
#         pair_set.add((i, judge))
#     pair_set.remove((judge, judge))
#     for f, s in trust:
#         if (f, s) in pair_set:
#             pair_set.remove((f, s))
#     return judge if len(pair_set) == 0 else -1


def find_judge(n, trust):
    count = [0] * (n + 1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i
    return -1


assert find_judge(2, [[1, 2]]) == 2
assert find_judge(3, [[1, 3], [2, 3]]) == 3
assert find_judge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert find_judge(3, [[1, 2], [2, 3]]) == -1
assert find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
