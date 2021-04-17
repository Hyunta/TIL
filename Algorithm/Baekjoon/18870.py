import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))
m2 = sorted(set(m))
d = {m2[i]: i for i in range(len(m2))}
res = [d[x] for x in m]
print(*res)

