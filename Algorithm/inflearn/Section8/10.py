n = int(input())
m = list(map(int, input().split()))
ch = int(input())
dy = [214000000]*(ch+1)

for x in m:
    dy[x] = 1
    for j in range(x,ch+1):
        if dy[j-x]+1 < dy[j]:
            dy[j] = dy[j-x]+1
print(dy[-1])