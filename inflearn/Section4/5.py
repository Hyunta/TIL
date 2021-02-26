n = int(input())
M = [tuple(map(int, input().split())) for _ in range(n)]
M=sorted(M, key=lambda x:(x[1],x[0]))

cnt=0
e=0
for m in M:
    if m[0] >= e:
        cnt += 1
        e = m[1]
print(cnt)
