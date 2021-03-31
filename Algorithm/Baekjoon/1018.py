n,m = map(int, input().split())
b = [list(x for x in str(input())) for _ in range(n)]
res=[]

for k in range(n-7):
    for l in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(k,k+8):
            for j in range(l,l+8):
                if (i+j)%2 == 0:
                    if b[i][j] != 'W' : cnt1 += 1
                    if b[i][j] != 'B' : cnt2 += 1
                else:
                    if b[i][j] != 'B' : cnt1 += 1
                    if b[i][j] != 'W' : cnt2 += 1
        res.append(min(cnt1,cnt2))
print(min(res))
print(res)
