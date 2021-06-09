import sys
input = sys.stdin.readline

n, m = map(int, input().split())
woods = list(map(int, input().split()))

start, end = 0, max(woods)


def countlog(num):
    cnt = 0
    for x in woods:
        if x > num:
            cnt += (x-num)
    return cnt


while start <= end:
    mid = (start + end) // 2
    log = countlog(mid)
    if log >= m:
        start = mid + 1
    elif log < m:
        end = mid - 1
print(end)
