import sys
input = sys.stdin.readline
n = int(input())

while n != 1:
    for x in range(2,n):
        if n % x == 0:
            print(x)
            return
    