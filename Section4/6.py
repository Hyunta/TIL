n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]

cnt=0
for h,w in M:
    for oh,ow in M:
        if h<oh and w<ow:
            cnt += 1
            break
print(n-cnt)

