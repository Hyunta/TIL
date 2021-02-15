n = int(input())
M=[]
for i in range(n):
        m = list(map(int, input().split()))
        m.insert(0,0)
        m.append(0)
        M.append(m)
M.insert(0,[])
M.append([])
'''
M.insert(0,[0]*n)
M.append([0]*n)
'''
for i in range(n+2):
    M[0].append(0)
    M[n+1].append(0)

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        m = M[i][j]
        if m > M[i-1][j] and m > M[i+1][j] and m > M[i][j+1] and m > M[i][j-1]:
            cnt += 1

print(cnt)