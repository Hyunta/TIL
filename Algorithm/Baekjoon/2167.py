import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
    tmp_r = 0
    i,j,x,y = map(int, input().split())
    for a in range(i-1,x):
        for b in range(j-1, y):
            tmp_r += arr[a][b]
    print(tmp_r)
