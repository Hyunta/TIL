t, lim = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(t)]
dy = [0]*(lim+1)

for [x,y] in m:
    for j in range(x,lim+1):
        if dy[j-x]+y > dy[j]:
            dy[j] = dy[j-x]+y
print(dy[-1])