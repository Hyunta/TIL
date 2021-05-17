def solution(m, n, puddles):
    res = list(([0]* (m+1) for _ in range(n+1)))
    for puddle in puddles:
        res[puddle[1]][puddle[0]] = -1
    res[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if res[i][j] >= 0:
                if res[i-1][j] > 0:
                    res[i][j] += res[i-1][j]
                if res[i][j-1] > 0:
                    res[i][j] += res[i][j-1]
    return res[n][m] % 1000000007