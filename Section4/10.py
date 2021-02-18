n = int(input())
a = list(map(int, input().split()))

s=[0]*n
for i in range(n):
    if i == 0:
        s[a[i]]=i+1
    else:
        cnt = 0
        for i2 in range(n):
            print("i=",i,"i2=",i2,s)
            if cnt == a[i]:
                if s[i2] == 0:
                    s[i2] = i+1
                    break
                else:
                    continue
            if s[i2] == 0:
                cnt += 1

for _ in s:            
    print(_,end=" ")
    