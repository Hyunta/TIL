n = int(input())
a = list(map(int, input().split()))

side=""
tot = []
last = 0
lt = 0
rt = n-1

while lt<=rt:
    if a[lt]>last:
        tot.append((a[lt],'L'))
    if a[rt]>last:
        tot.append((a[rt],'R'))
    tot.sort()
    if len(tot)==0:
        break
    else:
        side = side + tot[0][1]
        last = tot[0][0]
        if tot[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tot.clear()

print(len(side))
print(side)