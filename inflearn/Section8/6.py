n = int(input())
m = list()
for _ in range(n):
    (a,b,c) = map(int, input().split())
    m.append((a,b,c))
m.sort(reverse=True, key=lambda x:x[0])
m.insert(0,0)
dy = [0]*(n+1)
dy[1] = m[1][1]
for i in range(2,n+1):
    mx = 0
    for j in range(1,i+1):
        if m[j][2] > m[i][2] and dy[j]>mx:
            mx = dy[j]
    dy[i] = mx + m[i][1]
print(max(dy))

