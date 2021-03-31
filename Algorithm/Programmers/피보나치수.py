def solution(n):
    dy = [0 for _ in range(n+1)]
    dy[1] = 1
    dy[2] = 1
    for i in range(3,n+1):
        dy[i] = dy[i-2] + dy[i-1]
    return dy[n] % 1234567