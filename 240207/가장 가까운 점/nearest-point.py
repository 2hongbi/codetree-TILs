import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

pq = []

for x, y in points:
    heapq.heappush(pq, (abs(x) + abs(y), x, y))

for _ in range(m):
    dist, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (abs(x + 2) + abs(y + 2), x + 2, y + 2))
    

dist, x, y = pq[0]
print(x, y)