# A topological sort of a dag G = (V, E) is a linear ordering of all its vertices such that if G contains an edge
# (u,v), then u appears before v in the ordering. (If the graph contains a cycle, then no linear ordering is
# possible.) We can view a topological sort of a graph as an ordering of its vertices along a horizontal line so
# that all directed edges go from left to right. Many applications use directed acyclic graphs to indicate
# precedences among events.
from collections import defaultdict, deque


def topological_sort(g):
    def dfs(g, u):
        for v in g[u]:
            if v not in visited:
                dfs(g, v)
                visited.add(v)
        sortedv.appendleft(u)

    visited = set()
    sortedv = deque()
    for u in list(g):
        if u not in visited:
            dfs(g, u)
            visited.add(u)
    return sortedv


dress_order = [['shirt', 'tie'], ['tie', 'jacket'], ['jacket', None], ['belt', 'jacket'], ['shirt', 'belt'],
               ['watch', None], ['undershorts', 'pants'], ['pants', 'shoes'], ['socks', 'shoes'], ['shoes', None]]
g = defaultdict(list)
for u, v in dress_order:  # directed graph
    if v is None:
        g[u] = []
    else:
        g[u].append(v)
print(g)

print(topological_sort(g))
