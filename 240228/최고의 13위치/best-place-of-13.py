n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


ans = 0
for row in range(n):
    for col in range(n - 2):
        ans = max(ans, arr[row][col] + arr[row][col + 1] + arr[row][col + 2])

print(ans)