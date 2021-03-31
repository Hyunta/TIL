n,k = map(int, input().split())
li=list(map(int, input().split()))
res =[]

for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            res.append(li[i]+li[j]+li[l])

res = list(set(res))
res.sort(reverse=True)
print(res[k-1])