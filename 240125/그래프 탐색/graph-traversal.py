n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)] # index 1번부터 사용 위해
visited = [False] * (n + 1)

vertex_cnt = 0 # 간선 카운트

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    global vertex_cnt

    for v in graph[node]:
        if not visited[v]:
            visited[v] = True
            vertex_cnt += 1
            dfs(v)


visited[1] = True
dfs(1)

print(vertex_cnt)