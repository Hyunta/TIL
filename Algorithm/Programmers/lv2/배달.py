import sys

def solution(N, road, K):
    li = list([sys.maxsize] * N for _ in range(N))
    for a, b, c in road:
        if li[a - 1][b - 1] > c:
            li[a - 1][b - 1] = c
            li[b - 1][a - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                li[i][j] = min(li[i][j], li[i][k] + li[k][j])

    for z in range(N):
        li[z][z] = 0

    for x in li:
        print(x)
    cnt = 0
    for x in li[0]:
        if x <= K:
            cnt += 1
    return cnt