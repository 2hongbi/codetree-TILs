import sys
sys.setrecursionlimit(2500)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def initialize_zone():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] != k:
        return False
    return True

block_size = 0
def dfs(x, y, k):
    global block_size
    visited[x][y] = True
    block_size += 1

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)


max_block_size = 0
burst_blocks = 0

for k in range(1, 101):
    initialize_zone()
    current_max_block_size = 0
    current_burst_blocks = 0

    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                block_size = 0
                dfs(i, j, k)
                if block_size >= 4:
                    current_burst_blocks += 1
                current_max_block_size = max(current_burst_blocks, block_size)

        if current_burst_blocks > burst_blocks or (current_burst_blocks == burst_blocks and current_max_block_size > max_block_size):
            max_block_size = current_max_block_size
            burst_blocks = current_burst_blocks

print(burst_blocks, max_block_size)