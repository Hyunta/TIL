import sys
input = sys.stdin.readline

num = map(int, input().split())
res = 0
for x in num:
    res += x**2
print(res%10)