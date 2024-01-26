n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y) or visited[x][y] or grid[x][y] == 0:
        return False
    return True


def dfs(x, y):
    global people_count

    visited[x][y] = True
    people_count += 1

    # 상하좌우 네 방향에 대해 탐색
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)

people = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            people_count = 0
            dfs(i, j)
            people.append(people_count)

print(len(people))
for p in sorted(people):
    print(p)