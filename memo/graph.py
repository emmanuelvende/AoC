# Standard algos for graphs

def compute_neighbours(pos):
    return []


visited = set()


# Depth First Search
def dfs(visited, pos):  # pos := (col, row)
    if pos not in visited:
        visited.add(pos)
        neighbours = compute_neighbours(pos)
        # print(neighbours)
        for neighbour in neighbours:
            dfs(visited, neighbour)


# Breadth First Search
def bfs(visited, pos):
    queue = []
    visited.add(pos)
    queue.append(pos)
    while queue:
        s = queue.pop(0)
        for n in compute_neighbours(s):
            if n not in visited:
                visited.add(n)
                queue.append(n)
