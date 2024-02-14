n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

ans = 0
for c in coins:
    ans += k // c
    k %= c

print(ans)