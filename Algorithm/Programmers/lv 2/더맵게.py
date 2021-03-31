import heapq as hq
def solution(scoville, K):
    a = []
    cnt = 0
    for x in scoville:
        hq.heappush(a,x)
    while a[0]<K:
        hq.heappush(a, hq.heappop(a)+hq.heappop(a)*2)
        cnt += 1
        if len(a)==1 and a[0]<K:
            return -1
    return cnt