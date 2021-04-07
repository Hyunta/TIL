import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2,n):
        if n%x == 0:
            return False
    return True 

m = int(input())
n = int(input())
res=[]
for x in range(m,n+1):
    if isPrime(x):
        res.append(x)

if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)

