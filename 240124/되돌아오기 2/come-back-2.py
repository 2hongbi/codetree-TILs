x, y = 0, 0
dir_num = 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

ans = -1
sec = 0

commands = input()
for cmd in commands:
    if cmd == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    elif cmd == 'L':
        dir_num = (dir_num + 1) % 4
    elif cmd == 'R':
        dir_num = (dir_num - 1 + 4) % 4
    sec += 1
    if x == 0 and y == 0:
        ans = sec
        break

print(ans)