M=[]
for i in range(2):
    n = int(input())
    N = [int(x) for x in input().split()]
    '''
    for n in N:
        M.append(n)
    '''
    M=M+N
for m in sorted(M):
    print(m, end=" ")