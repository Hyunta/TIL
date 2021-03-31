import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x:x[1])

print(li)
cnt = 0
last = 0
for x in li:
    if x[0] >= last:
        last = x[1]
        cnt += 1
print(cnt)

