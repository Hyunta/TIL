l=len(numbers)
res=[]
for i in range(l):
    for j in range(i+1,l):
        res.append(numbers[i]+numbers[j])
sorted(list(set(res)))