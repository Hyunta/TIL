import sys
def checkprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

input = sys.stdin.readline
n = input()
li = list(map(int, input().split()))
cnt = 0
for x in li:
    if checkprime(x):
        cnt += 1
print(cnt)