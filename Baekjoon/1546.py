n=int(input())
li = list(map(int, input().split()))
m=max(li)

res=[]
for x in li:
    res.append(x/m*100)

print(sum(res)/n)