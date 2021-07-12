import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]
items = [[0,0]]
for _ in range(n):
    items.append((list(map(int, input().split()))))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i][0]
        v = items[i][1]
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v + bag[i-1][j-w], bag[i-1][j])
print(bag[n][k])


