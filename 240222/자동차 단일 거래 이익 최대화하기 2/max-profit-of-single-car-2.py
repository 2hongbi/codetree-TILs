n = int(input())
prices = list(map(int, input().split()))

ans = 0

for i in range(n):
    car = prices[i]

    for j in range(i + 1, n):
        if prices[j] > car:
            profit = prices[j] - car
            ans = max(ans, profit)

print(ans)