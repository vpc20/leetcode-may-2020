from collections import defaultdict

WHITE = 0  # undiscovered
GRAY = 1  # discovered
BLACK = 2  # finished


def is_directed_acyclic_graph(g):
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

    colors = {}  # vertex colors
    for u in list(g):
        colors[u] = WHITE

    for u in list(g):
        if colors[u] == WHITE:
            if not dfs(g, u):
                return False
    return True


dress_order = [['shirt', 'tie'], ['tie', 'jacket'], ['jacket', None], ['belt', 'jacket'], ['shirt', 'belt'],
               ['watch', None], ['undershorts', 'pants'], ['pants', 'shoes'], ['socks', 'shoes'], ['shoes', None]]
g = defaultdict(list)
for u, v in dress_order:  # directed graph
    if v is None:
        g[u] = []
    else:
        g[u].append(v)
print(g)

print(is_directed_acyclic_graph(g))
