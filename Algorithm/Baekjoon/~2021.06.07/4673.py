m=list(range(1,10001))
n=list(range(1,10001))

for x in m:
    sum = x
    for y in str(x):
        sum += int(y)
    if sum in n:
        n.remove(sum)
for z in n:
    print(z)