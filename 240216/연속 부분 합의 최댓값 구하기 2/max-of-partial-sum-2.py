import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

ans = -sys.maxsize

total = 0

for i in range(1, n + 1):
    if total < 0:
        total = arr[i]
    else:
        total += arr[i]
    ans = max(ans, total)

print(ans)