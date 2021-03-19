n = int(input())
i1=0
i2=1
li=[i1,i2]
for _ in range(10):
    i1 = i1 + i2
    i2 = i1 + i2
    li.append(i1)
    li.append(i2)

print(li[n])