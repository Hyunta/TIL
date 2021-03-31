n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]
M.sort(reverse=True)

max_weight=0
cnt=0
for height,weight in M:
    if weight > max_weight:
        cnt+=1
        max_weight=weight

print(cnt)

