def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

n = int(input())
m = map(int, input().split())
for x in m:
    x = reverse(x)
    if isPrime(x):
        print(x, end=' ')
