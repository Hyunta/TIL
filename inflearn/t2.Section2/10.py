n = int(input())
m = list(map(int, input().split()))

cnt = 0
tot = 0
for x in m:
    if x == 1:
        tot += 1+cnt
        cnt += 1
    else:
        cnt = 0
print(tot)
