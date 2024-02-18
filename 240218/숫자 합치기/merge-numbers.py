import heapq

n = int(input())
numbers = list(map(int, input().split()))

pq = numbers
heapq.heapify(pq)

ans = 0

while len(pq) > 1: # 하나의 숫자만 남을 때까지 반복
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)

    cost = first + second
    ans += cost

    heapq.heappush(pq, cost)

print(ans)