n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_k = 0
for row in grid:
    temp = max(row)
    max_k = max(max_k, temp)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] < k:
        return False
    return True

def dfs(x, y, k):
    global cnt

    visited[x][y] = True
    cnt += 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)

count_list = list()
visited = [[False] * m for _ in range(n)]
cnt = 0
for k in range(1, max_k + 1):
    for i in range(n):
        for j in range(m):
            if grid[i][j] < k and not visited[i][j]:
                cnt += 1
                dfs(i, j, k)
                count_list.append(cnt)
                visited = [[False] * m for _ in range(n)]

print(count_list)