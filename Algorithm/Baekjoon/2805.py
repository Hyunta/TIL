import sys
input = sys.stdin.readline

n, m = map(int, input().split())
woods = list(map(int, input().split()))

start, end = 0, max(woods)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for wood in woods:
        if wood > mid:
            log += wood - mid

    if log >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)