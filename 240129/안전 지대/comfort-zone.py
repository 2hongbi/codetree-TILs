import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[False] * m for _ in range(n)]

zone_num = 0

def initialize_zone():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    return True

def dfs(x, y, k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)

def get_zone(k):
    global zone_num

    zone_num = 0
    initialize_zone()

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                zone_num += 1
                visited[i][j] = True
                dfs(i, j, k)

max_zone_num = -1
answer_k = 0
max_height = 100

for k in range(1, max_height + 1):
    get_zone(k)

    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)