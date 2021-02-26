n, m = map(int, input().split())
s = list([0 for _ in range(n)] for _ in range(n))

for _ in range(m):
    x,y = map(int, input().split())
    s[x-1][y-1] = 1

print(s)
