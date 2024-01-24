n = int(input())

dir_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

dir_num = 0
x, y = 0, 0

ans = -1
sec = 0

def move(move_dir, dist):
    global x, y
    global ans, sec

    for _ in range(dist):
        x, y = x + dxs[move_dir], y + dys[move_dir]

        sec += 1

        if x == 0 and y == 0:
            ans = sec
            return True
    return False


for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)

    move_dir = dir_dict[c_dir]

    # 이동
    move_done = move(move_dir, dist)

    # 시작 위치에 도달했다면 종료
    if move_done:
        break

print(ans)