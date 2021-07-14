#최소 힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    print(heap)
    tmp = int(input())
    if tmp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, tmp)
