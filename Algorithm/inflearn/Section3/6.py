n = int(input())
M = []
for i in range(n):
    m = list(map(int, input().split()))
    M.append(m)

tot = 0

#가로줄 덧셈
for i in range(n):
    s1 = sum(M[i])
    if s1> tot:
        tot =s1

#세로줄 덧셈
for j in range(n):
    s2=0
    for i in range(n):
        s2 = M[i][j]+s2
    if s2 > tot:
        tot = s2

#대각선 덧셈
if n%2 != 0:
    s3 = 0
    s4 = 0
    for i in range(n):
        s3 = M[i][i] + s3
        if s3 > tot:
            tot = s3
        s4 = M[i][n-1-i]+s4
        if s4 > tot:
            tot = s4
print(tot)
