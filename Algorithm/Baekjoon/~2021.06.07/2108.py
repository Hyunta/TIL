import sys
n = int(input())
li = [int(sys.stdin.readline()) for _ in range(n)]
d = dict()
res=[]
for x in li:
    d[x] = d.get(x,0)+1
for x,y in d.items():
    if y == max(d.values()):
        res.append(x)
res.sort()

print(round(sum(li)/n))
print(sorted(li)[n//2])
if len(res) == 1:
    print(res[0])
else:
    print(res[1])
print(max(li)-min(li))