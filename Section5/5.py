n, k = map(int, input().split())
Q=list(range(1,n+1))

cnt = 0

while len(Q) != 1:
    Q.append(Q.pop(0))
    cnt += 1
    if cnt%k == 0:
        Q.pop()
print(Q[0])
    


