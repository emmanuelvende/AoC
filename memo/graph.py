# Standard algos for graphs

def get_neighbours(node):
    return []

def process(node):
    print(node)

# Depth First Search
def dfs(graph, node):
    def _dfs(graph, visited, node):
        if node not in visited:
            visited.add(node)
            process(node)
            for n in get_neighbours(graph, node):
                _dfs(graph, visited, n)

    visited = set()
    _dfs(graph, visited, node)


# Breadth First Search
def bfs(graph, node):
    visited = set()
    queue = []
    visited.add(node)
    queue.append(node)
    while queue:
        x = queue.pop(0)
        process(x)
        for n in get_neighbours(graph, x):
            if n not in visited:
                visited.add(n)
                queue.append(n)