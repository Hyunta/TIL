n = int(input())
li = list(map(int,input().split()))
mx = 0
v= 0
for x in li:
    tmp = 0
    for i in range(len(str(x))):
        tmp += int(str(x)[i])
    if tmp > mx:
        mx = tmp
        v = x
print(v)

    
    
