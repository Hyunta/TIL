from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
g, s = map(int, input().split())
st = [list(map(int, input().split())) for _ in range(s)]
ch = [[0]*g for _ in range(s)]
L = 0
Q= deque()

for x in range(s):
    for y in range(g):
        if st[x][y] == 1:
            Q.append((x, y))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        a = tmp[0]+dx[i]
        b = tmp[1]+dy[i]
        if 0 <= a < s and 0 <= b < g and st[a][b] == 0:
            st[a][b] = 1
            ch[a][b] = ch[tmp[0]][tmp[1]]+1
            Q.append((a, b))
'''
    print("st=")
    for z in st:
        print(z)
    print("ch=")
    for x in ch:
        print(x)
    print()
'''
sts = [x for y in st for x in y]
res = [x for y in ch for x in y]
if 0 in sts:
    print(-1)
else:
    print(max(res))