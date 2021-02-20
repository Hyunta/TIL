n,m = map(int, input().split())
li =[(k,v) for k,v in enumerate(list(map(int, input().split())))] 

cnt = 0

while True:
    p = li.pop(0)
    if any(p[1]<x[1] for x in li):
        li.append(p)
    else:
        cnt += 1
        if p[0] == m:
            print(cnt)
            break
        
