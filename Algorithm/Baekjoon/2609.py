import sys
input = sys.stdin.readline
n,m = map(int, input().split())
x,y = n,m

while y!= 0:
    x = x%y
    x,y = y,x

print(x)
print(n*m//x)