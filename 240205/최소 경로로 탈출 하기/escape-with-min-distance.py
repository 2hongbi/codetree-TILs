from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False for _ in range(m)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    
    while queue:
        x, y, dist = queue.popleft()
        if x == n - 1 and y == m - 1: # 목적지 도달 시 바로 반환
            return dist
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True
                

    # 목적지에 도달할 수 없는 경우
    return -1


print(bfs(0, 0))