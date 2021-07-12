import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_hq, min_hq = [], []

for _ in range(n):
    tmp = int(input())
    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, (-tmp, tmp))
    else:
        heapq.heappush(min_hq, (tmp, tmp))

    if min_hq and max_hq[0][1] > min_hq[0][1]:
        tmp_max = heapq.heappop(max_hq)[1]
        tmp_min = heapq.heappop(min_hq)[1]
        heapq.heappush(max_hq, (-tmp_min, tmp_min))
        heapq.heappush(min_hq, (tmp_max, tmp_max))
    print(max_hq[0][1])

