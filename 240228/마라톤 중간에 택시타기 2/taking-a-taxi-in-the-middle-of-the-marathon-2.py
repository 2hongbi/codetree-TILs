import sys

n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

for i in range(1, n - 1):
    dist = 0
    prev_idx = 0
    for j in range(1, n):
        if j == i:
            continue
        dist += abs(checkpoints[prev_idx][0] - checkpoints[j][0]) + abs(checkpoints[prev_idx][1] - checkpoints[j][1])
        prev_idx = j

    ans = min(ans, dist)

print(ans)