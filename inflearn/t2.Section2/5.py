n,m = map(int, input().split())
d = dict()

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i+j]=d.get(i+j,0)+1

for k,v in d.items():
    if v == max(d.values()):
        print(k, end=' ')