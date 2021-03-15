n = int(input())
m=[list(map(int,input().split())) for _ in range(n)]
print(m)
m.sort(key=lambda x: x[1])
print(m)

cnt=0
e=0
for x in m:
    if x[0] >= e:
        cnt += 1
        e = x[1]
print(cnt)