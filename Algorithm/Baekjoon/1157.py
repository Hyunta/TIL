s=str(input())
d = dict()
li=[]
for x in s.upper():
    d[x] = d.get(x,0)+1
for x,v in d.items():
    if v == max(d.values()):
        li.append(x)
if len(li) == 1:
    print(li[0])
else:
    print("?")