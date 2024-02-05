from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1

bfs(0, 0)
if visited[n - 1][n - 1]:
    print(grid[n - 1][n - 1] - 1)
else:
    print(-1)