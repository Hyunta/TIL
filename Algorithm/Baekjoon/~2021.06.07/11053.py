import sys
input = sys.stdin.readline

a = int(input())
arr = [0]
arr += map(int, input().split())
dy = [0] * (a+1)
dy[1] = 1
for i in range(2,a+1):
    mx = 0
    for j in range(1,i):
        if arr[i] > arr[j] and dy[j] > mx:
                mx = dy[j]
    dy[i] = mx +1
print(max(dy))
