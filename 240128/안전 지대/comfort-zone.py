n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    return in_range(x, y) and not visited[x][y] and grid[x][y] > k

def dfs(x, y, k):
    visited[x][y] = True

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)


max_safe_area = 0
best_k = 0

for k in range(101):  # 높이의 최대값은 100이므로
    visited = [[False] * m for _ in range(n)]
    safe_area_count = 0

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                dfs(i, j, k)
                safe_area_count += 1

    if safe_area_count > max_safe_area:
        max_safe_area = safe_area_count
        best_k = k

print(best_k, max_safe_area)