import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []

for a in arr:
    heapq.heappush(pq, -a)

while len(pq) > 1:

    num1 = -heapq.heappop(pq)
    num2 = -heapq.heappop(pq)

    if num1 - num2 != 0:
        heapq.heappush(pq, -(num1 - num2))



if len(pq) == 0:
    print(-1)
else:
    print(-pq[0])