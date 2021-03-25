import sys
n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort(key=lambda x: [x[0],x[1]])
for x in li:
    print(x[0],x[1])