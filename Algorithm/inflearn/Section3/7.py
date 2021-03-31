n = int(input())
M = []
for i in range(n):
    m = list(map(int, input().split()))
    M.append(m)

tot = 0
a = round((n+1)/2)-1
d = 0

for i in range(a+1):
    for j in range(n):
        if a-d <= j and j <= a+d:
            tot = M[i][j] + tot
        elif j > a+d:
            d += 1
            break

for i in range(a+1, n):
    d-=1
    for j in range(n):
        if a-d <= j and j <= a+d:
            tot = M[i][j] + tot

print(tot)
