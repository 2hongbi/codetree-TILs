n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

max_k = 1  # 안전 영역이 최대일 경우 k값
max_cnt = 0  # 안전 영역의 수 


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    return in_range(x, y) and not visited[x][y] and graph[x][y] > k

def dfs(x, y, k):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)

# 주어진 k의 범위 1 <= k <= 100
for k in range(1, 101):
    cnt_of_areas = 0
    for x in range(n):
        for y in range(m):
            if can_go(x, y, k):
                cnt_of_areas += 1
                dfs(x, y, k)
    
    if max_cnt < cnt_of_areas:
        max_k = k
        max_cnt = cnt_of_areas

    for i in range(n): # 다음 시뮬레이션 위해 초기화
        for j in range(m):
            visited[i][j] = False

print(max_k, max_cnt)