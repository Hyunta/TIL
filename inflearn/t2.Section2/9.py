n = int(input())

scr=[]
for _ in range(n):
    tmp = list(map(int,input().split()))
    if len(set(tmp)) == 1:
        scr.append(10000 + 1000*tmp[0])
    elif len(set(tmp)) == 3:
        scr.append(max(tmp)*100)
    else:
        if tmp.count(tmp[0]) == 2:
            scr.append(1000+tmp[0]*100)
        else:
            scr.append(1000+tmp[1]*100)
print(max(scr))