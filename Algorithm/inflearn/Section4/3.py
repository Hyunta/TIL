n,m = map(int, input().split())
pl=list(map(int,input().split()))

def Count(time):
    sum = 0
    cnt = 0
    for s in li:
        if sum+s >= time:
            cnt +=1
            sum = s
        else:
            sum += s
    return cnt

lt = 1
rt = sum(pl)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
     
