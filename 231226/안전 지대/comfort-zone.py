import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

zone_num = 0

def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    return in_range(x, y) and not visited[x][y] and grid[x][y] > k

def dfs(x, y, k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)

def get_zone_num(k):
    global zone_num

    zone_num = 0
    initialize_visited()

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                zone_num += 1

                dfs(i, j, k)

max_zone_num = -1
answer_k = 0
max_height = 100

for k in range(1, max_height + 1):
    get_zone_num(k)

    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)