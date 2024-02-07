import heapq

n = int(input())

pq = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if not pq:
            print(0)
        else:
            print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -x)