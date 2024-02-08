import heapq
import sys

n = int(input())
arr = list(map(int, input().split()))

pq = []

for a in arr:
    heapq.heappush(pq, a)

avg = -sys.maxsize
for _ in range(n - 2):
    heapq.heappop(pq)

    avg = max(avg, sum(pq) / len(pq))

print(f"{avg:.2f}")