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
    def dfs(g, u):
        colors[u] = GRAY
        for v in g[u]:
            if colors[v] == WHITE:
                if not dfs(g, v):
                    return False
            elif colors[v] == GRAY:
                return False
        colors[u] = BLACK
        return True

    if not preqs:
        return True
    g = defaultdict(list)  # graph for prerequisites
    for v2, v1 in preqs:  # directed graph
        g[v1].append(v2)
    print(g)

    colors = {}  # vertex colors
    for u in range(n):
        colors[u] = WHITE

    for u in list(g):
        if colors[u] == WHITE:
            if not dfs(g, u):
                return False
    return True


print(can_finish(1, []))
print(can_finish(2, [[1, 0]]))
print(can_finish(3, [[2, 1], [1, 0]]))
print(can_finish(4, [[3, 2], [2, 1], [1, 0]]))
print(can_finish(4, [[1, 2], [3, 2], [2, 1], [1, 0]]))
print(can_finish(5, [[1, 0], [2, 1], [3, 4], [4, 3]]))
