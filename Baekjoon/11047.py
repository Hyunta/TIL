import sys
n,k = map(int, sys.stdin.readline().split())
li =[]
for _ in range(n):
    li.insert(0, int(sys.stdin.readline()))

cnt = 0
for x in li:
    while k > 0:
        if k - x < 0:
            break
        else:
            cnt += k//x
            k = k%x
print(cnt)