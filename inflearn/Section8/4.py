n = int(input())
m = list(map(int, input().split()))
m.insert(0,0)
dy= [0]*(n+1)
dy[1] = 1
res = 0
for i in range(2,n+1):
    max = 0
    for j in range(1,i):
        if m[i]> m[j] and dy[j]>max:
            max = dy[j]
    dy[i] = max +1
    if dy[i] > res:
        res = dy[i]
print(res)