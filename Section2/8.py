N = int(input())
M = [int(x) for x in input().split()]

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x ==1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True


for i,m in enumerate(M):
    if isPrime(reverse(m)):
        print(reverse(m), end=' ')
  