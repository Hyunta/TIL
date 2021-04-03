import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int, input().split())
li = [i for i in range(1,n+1)]
res = list(combinations(li,m))
for x in res:
    for i in x:
        print(i, end=' ')
    print()
