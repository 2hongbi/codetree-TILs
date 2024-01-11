x, y = 0, 0

directions = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())
for _ in range(n):
    dir, num = input().split()
    d = directions[dir]
    x, y = x + (int(num) * dx[d]), y + (int(num) * dy[d])

print(x, y)