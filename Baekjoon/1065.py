n = int(input())
cnt=0
for i in range(1,n+1):
    if i < 100:
        cnt+= 1
    else:
        nl = list(map(int, str(i)))
        if nl[0] - nl[1] == nl[1] - nl[2]:
            cnt += 1
print(cnt)