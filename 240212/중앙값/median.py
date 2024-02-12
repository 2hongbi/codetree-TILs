import heapq

n = int(input())


for _ in range(n):
    min_heap = [] # 최소 힙
    max_heap = [] # 최대 힙; 원소를 음수로 저장 -> 최대힙 구현

    t = int(input())
    arr = list(map(int, input().split()))

    idx = 1
    for a in arr:
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -a)
        else:
            heapq.heappush(min_heap, a)

        if min_heap and -max_heap[0] > min_heap[0]:
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)

        if idx % 2 == 1:
            print(-max_heap[0], end=' ')
        idx += 1
    print()