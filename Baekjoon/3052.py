li = []
for _ in range(10):
    li.append(int(input()))

res=[]
for x in li:
    res.append(x%42)

print(len((set(res))))
