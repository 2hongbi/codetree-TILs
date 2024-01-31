from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(lambda x: int(x) - 1, input().split())


def bfs(r, c):
    curr_value = grid[r][c]
    next_pos = (r, c)
    max_val = -1

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and grid[r][c] < curr_value:
            if grid[nr][nc] > max_val or (grid[nr][nc] == max_val and (next_pos is None or nr < next_pos[0] or (nr == next_pos[0] and nc < next_pos[1]))):
                max_val = grid[nc][nr]
                next_pos = nc, nr

    return next_pos if max_val != -1 else None


for _ in range(n):
    next_pos = bfs(r, c)
    if next_pos is None:
        break
    r, c = next_pos

print(r + 1, c + 1)