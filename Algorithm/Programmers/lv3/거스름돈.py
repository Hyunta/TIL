def solution(n, money):
    dy = [0] * (n+1)
    for x in money:
        dy[x] += 1
        for y in range(x+1,n+1):
            dy[y] += dy[y-x]
    return dy[n]