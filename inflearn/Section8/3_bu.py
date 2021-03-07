n = int(input())
dy = [0]*(n+1)
dy[1]=2
dy[2]=3
for i in range(3,n+1):
    dy[i] = dy[i-1]+dy[i-2]
print(dy[n])