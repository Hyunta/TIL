def count(len):
    b = min(B)
    cnt = 1
    for num in B:
        if num >= b+len:
            cnt +=1
            b = num
    return cnt

n,c = map(int, input().split())
B=[]
for _ in range(n):
    x = int(input())
    B.append(x)
B.sort()


lt = min(B)
rt = max(B)
res=0

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
