from itertools import chain

def solution(n):
    route = [[0] * i for i in range(1,n+1)]
    x, y, num = -1, 0, 1

    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            route[x][y] = num
            num += 1

    return list(chain(*route))


print(solution(4))
print(solution(5))
print(solution(6))
