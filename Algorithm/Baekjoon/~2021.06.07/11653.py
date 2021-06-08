
import sys
input = sys.stdin.readline
'''
n = int(input())

while n != 1:
    for x in range(2,n+1):
        if n % x == 0:
            print(x)
            n = n // x
            break
'''

n = int(input())

if n == 2:
    print(2)
else:
    i = 2
    while n != 1:
        if n % i == 0:
            n /= i
            print(i)
        else:
            i += 1
            
        if i > (n**0.5):
            print(int(n))
            N /= N