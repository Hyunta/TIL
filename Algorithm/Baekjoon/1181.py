import sys
input = sys.stdin.readline

n = int(input())
m=[]
for _ in range(n):
    m.append(input().rstrip())

m = list(set(m))
m.sort(key=lambda x: (len(x),x))
for x in m:
    print(x)