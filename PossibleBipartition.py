# Given a set of N people(numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group. Formally,
# if dislikes[i] =[a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
# Example 1:
# Input: N = 4, dislikes = [[1, 2], [1, 3], [2, 4]]
# Output: true
# Explanation: group1[1, 4], group2[2, 3]
#
# Example 2:
# Input: N = 3, dislikes = [[1, 2], [1, 3], [2, 3]]
# Output: false
#
# Example 3:
# Input: N = 5, dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# Output: false
#
# Note:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
#
from collections import defaultdict, deque


def possible_bipartition(n, dislikes):
    if not dislikes:
        return True

    g = defaultdict(list)  # graph for dislikes
    for v1, v2 in dislikes:  # undirected graph
        g[v1].append(v2)
        g[v2].append(v1)
    colors = {}  # color could be 1 or -1
    q = deque()

    # bfs traversal
    for v in list(g):  # iterate through vertices
        if v not in colors:
            colors[v] = 1
            q.append(v)
            while q:
                v = q.popleft()
                color = -colors[v]
                for nb in g[v]:  # iterate through neighbors of vertex
                    if nb not in colors:
                        colors[nb] = color
                        q.append(nb)
                    elif colors[nb] == colors[v]:
                        return False
    return True


# def possible_bipartition(n, dislikes):
#     g = defaultdict(list)  # graph for dislikes
#     for v1, v2 in dislikes:
#         g[v1].append(v2)
#         g[v2].append(v1)
#     print(g)
#     visited = set()
#     q = deque()
#     colors = defaultdict(int)
#     color = 0
#
#     # bfs traversal
#     for v in list(g):  # iterate through vertices
#         if v not in visited:
#             # print(v, end=' ')
#             colors[v] = color
#             q.append(v)
#             visited.add(v)
#         while q:
#             v = q.popleft()
#             color = 1 - colors[v]
#             for nb in g[v]:  # iterate through neighbors of vertex
#                 if nb not in visited:
#                     # print(nb, end=' ')
#                     colors[nb] = color
#                     q.append(nb)
#                     visited.add(nb)
#                 elif colors[nb] == colors[v]:
#                     return False
#     return True


# def possible_bipartition(n, dislikes):
#     nset1 = set()
#     nset2 = set()
#     for i, j in dislikes:
#         if i not in nset1:
#             if i in nset2:
#                 return False
#             nset1.add(i)
#             if j in nset1:
#                 return False
#             nset2.add(j)
#         else:
#             if i in nset2:
#                 return False
#             if j in nset1:
#                 return False
#             nset2.add(j)
#     return True


assert possible_bipartition(4, [[1, 2], [1, 3], [2, 4]]) is True
assert possible_bipartition(3, [[1, 2], [1, 3], [2, 3]]) is False
assert possible_bipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) is False
# print(possible_bipartition(10, [[6, 9], [1, 3], [4, 8], [5, 6], [2, 8], [4, 7], [8, 9], [2, 5], [5, 8], [1, 2], [6, 7],
#                                 [3, 10], [8, 10], [1, 5], [3, 6], [1, 10], [7, 9], [4, 10], [7, 10], [1, 4], [9, 10],
#                                 [4, 6], [2, 7], [6, 8], [5, 7], [3, 8], [1, 8], [1, 7], [7, 8], [2, 4]]))
assert possible_bipartition(10,
                            [[4, 7], [4, 8], [5, 6], [1, 6], [3, 7], [2, 5], [5, 8], [1, 2], [4, 9], [6, 10], [8, 10],
                             [3, 6], [2, 10], [9, 10], [3, 9], [2, 3], [1, 9], [4, 6], [5, 7], [3, 8], [1, 8], [1, 7],
                             [2, 4]]) is True
