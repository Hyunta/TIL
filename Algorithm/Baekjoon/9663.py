import sys
input = sys.stdin.readline

n = int(input())


def DFS(q, r, n):
    cnt = 0
    if n == r:
        return 1
    for c in range(n):
        q[r] = c
        for i in range(r):
            if q[i] == q [r]:
                break
            if abs(q[i]-q[r]) == r -i :
                break
        else:
            cnt += DFS(q, r+1, n)
    return cnt

print(DFS([0]*n, 0, n))