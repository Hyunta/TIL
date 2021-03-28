import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()
tot = 0
for i in range(n):   
    tot += sum(m[:i+1])
print(tot)