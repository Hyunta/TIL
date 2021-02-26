def get_num(M,n):
    for i in range(n):
        m=list(map(int, input().split()))
        M.append(m)

def list_shift(M,d,a):
    if a>len(M):
        a = a % len(M)
    if d == 0:
        return M[a:]+M[:a]
    elif d == 1:
        return M[-a:]+M[:-a]
        
M = []
R = []

n1 = int(input())
get_num(M,n1)
n2 = int(input())
get_num(R,n2)

for li in R:
    M[li[0]-1] = list_shift(M[li[0]-1],li[1],li[2])

tot=0
for k,v in enumerate(M):
    if k < n1//2:
        tot += sum(v[k:n1-k])
    else:
        tot += sum(v[n1-k-1:k+1])
print(tot)
