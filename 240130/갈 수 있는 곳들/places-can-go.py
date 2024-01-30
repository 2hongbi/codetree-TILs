from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
starts = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

visited = [[False] * n for _ in range(n)]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    count = 1 # 현재 시작점 포함해 카운트 시작

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count


total_count = 0
for r, c in starts:
    if not visited[r][c]:
        total_count += bfs(r, c)

print(total_count)