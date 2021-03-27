import sys
n = int(sys.stdin.readline())
m=[]
for _ in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))

m.sort(key=lambda x: [x[1],x[0]])
for x in m:
    print(x[0],x[1])