n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, weight = map(int, input().split())
    tree[a].append((b, weight))
    tree[b].append((a, weight))

def dfs(start, visited):
    stack = [(start, 0)]
    visited[start] = True
    max_distance = 0
    max_node = start

    while stack:
        current, distance = stack.pop()
        if distance > max_distance:
            max_distance = distance
            max_node = current
        for next, weight in tree[current]:
            if not visited[next]:
                visited[next] = True
                stack.append((next, distance + weight))

    return max_node, max_distance


visited = [False] * (n + 1)
farthest_node, _ = dfs(1, visited)

visited = [False] * (n + 1)
_, diameter = dfs(farthest_node, visited)

print(diameter)