# 그냥 sort를 이용한 풀이 효율성 0점
def solution(n, works):
    res = 0
    for _ in range(n):
        works.sort()
        if works[-1]-1 < 0:
            break
        works[-1] -= 1
    for x in works:
        res += x*x
    return res

# 힙큐를 이용한 풀이, 복잡하지만 만점
import heapq as hq
def solution2(n, works):
    h = []
    for work in works:
        hq.heappush(h,[-work,work])
    for _ in range(n):
        tmp = hq.heappop(h)[1]
        if tmp-1 < 0:
            hq.heappush(h,[-tmp,tmp])
            return 0
            break
        tmp -= 1
        hq.heappush(h,[-tmp,tmp])
    print(h)
    res = 0
    for x in h:
        res += x[1]**2
    return res