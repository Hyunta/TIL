N=[]
for i in range(1,21):
    N.append(i)

for i in range(10):
    m,n = map(int, input().split())
    N[m-1:n]=N[m-1:n][::-1]

for i in N:
    print(i, end=" ")