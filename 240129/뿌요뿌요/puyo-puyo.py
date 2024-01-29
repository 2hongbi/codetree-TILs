n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] != k:
        return False
    return True


def dfs(x, y, k):
    global cnt, max_value
    visited[x][y] = True
    cnt += 1

    k = grid[x][y]

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)
    if cnt >= 4:
        return True
    else:
        return False

max_value = -1
max_cnt = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j, 0):
            max_value = max(max_value, cnt)
            max_cnt += 1
        else:
            max_value = max(max_value, cnt)

print(max_cnt, max_value)