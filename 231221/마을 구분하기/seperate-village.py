n = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

people_num = 0
people_nums = list()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global people_num

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = dx + x, dy + y

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True

            people_num += 1
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            people_num = 1

            dfs(i, j)

            # 한 마을에 대한 탐색이 끝난 경우 마을 내의 사람 수 저장
            people_nums.append(people_num)

# 각 마을 내 사람의 수를 오름차순으로 정렬
people_nums.sort()

print(len(people_nums))

for i in range(len(people_nums)):
    print(people_nums[i])