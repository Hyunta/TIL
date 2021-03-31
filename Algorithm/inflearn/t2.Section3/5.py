import sys
n,m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    sum = 0
    if li[i] > m:
        continue
    for j in range(i,n):
        sum += li[j]
        if sum == m:
            cnt += 1
            break
        elif sum > m:
            break
print(cnt)