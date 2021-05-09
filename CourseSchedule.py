# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Some courses may
# have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
# as a pair: [0, 1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is
# possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: false
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to
# take course 0 you should also have finished course 1. So it is impossible.
#
# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.Read more about how a
# graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10 ^ 5
from collections import defaultdict

WHITE = 0  # undiscovered
GRAY = 1  # discovered
BLACK = 2  # finished


def can_finish(n, preqs):
    def dfs(u):
        colors[u] = GRAY
        for v in g[u]:
            if colors[v] == WHITE:
                if not dfs(v):
                    return False
            elif colors[v] == GRAY:
                return False
        colors[u] = BLACK
        return True

    if not preqs:
        return True
    g = defaultdict(list)  # graph for prerequisites
    for v, u in preqs:  # directed graph
        g[u].append(v)
    # print(g)

    colors = {}  # vertex colors
    for u in range(n):
        colors[u] = WHITE

    for u in list(g):
        if colors[u] == WHITE:
            if not dfs(u):
                return False
    return True


# def can_finish(n, preqs):
#     def dfs(u):
#         visited.add(u)
#         cycles.add(u)
#         for v in g[u]:
#             if v not in visited:
#                 if not dfs(v):
#                     return False
#             elif v in cycles:
#                 return False
#         cycles.remove(u)
#         return True
#
#     if not preqs:
#         return True
#     g = defaultdict(list)  # graph for prerequisites
#     for i in range(n):
#         g[i] = []
#     for v, u in preqs:  # directed graph
#         g[u].append(v)
#     print(g)
#
#     visited = set()
#     cycles = set()
#     for u in list(g):
#         if u not in visited:
#             if not dfs(u):
#                 return False
#     return True


# print(can_finish(1, []))
# print(can_finish(2, [[1, 0]]))
# print(can_finish(3, [[2, 1], [1, 0]]))
# print(can_finish(4, [[3, 2], [2, 1], [1, 0]]))
# print(can_finish(4, [[1, 2], [3, 2], [2, 1], [1, 0]]))
# print(can_finish(5, [[1, 0], [2, 1], [3, 4], [4, 3]]))
# print(can_finish(5, [[1, 0], [2, 1], [4, 3], [2, 4]]))
# print(can_finish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))

assert can_finish(2, [[1, 0], [0, 1]]) is False
assert can_finish(3, [[1, 0], [2, 1], [0, 2]]) is False
assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True

# l = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
# l = [[1, 0], [2, 0], [3, 1], [3, 2]]
# print([(e[1], e[0]) for e in l])
