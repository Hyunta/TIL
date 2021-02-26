n = int(input())
for _ in range(n):
    m = list(map(int, input().split()))
    num = m.pop(0)
    mv = sum(m)/num
    cnt = 0
    for x in m:
        if x > mv :
            cnt += 1
    print('%0.3f' % round(cnt/num*100, 3),"%",sep='')
