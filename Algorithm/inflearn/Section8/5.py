n = int(input())
m = list(map(int, input().split()))
m.insert(0,0)
dy = [0]*(n+1)
dy[1]=1
for i in range(2, n+1):
    mx = 0
    for j in range(1,i+1):
        if m[i]>m[j] and dy[j]>mx:
            mx = dy[j]
    dy[i] = mx +1
print(max(dy))
        