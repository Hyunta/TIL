import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 2:
        print(2**(n-1))
        continue
    dy = [0] * (n+1)
    dy[1] = 1
    dy[2] = 2
    dy[3] = 4
    for i in range(4,n+1):
        dy[i] += dy[i-1]
        dy[i] += dy[i-2]
        dy[i] += dy[i-3]
    print(dy[n])
