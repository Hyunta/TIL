def Count(m):
    cnt=0
    for l in len:
        cnt += (l//m)
    return cnt

k,n = map(int, input().split())
len = [int(input()) for _ in range(k)]


lt = 1
rt = max(len)
res=0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)