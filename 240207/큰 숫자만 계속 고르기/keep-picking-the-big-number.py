import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pq = []

for a in arr:
    heapq.heappush(pq, -a)

for _ in range(m):
    temp = -(heapq.heappop(pq)) - 1
    heapq.heappush(pq, -temp)

print(-pq[0])