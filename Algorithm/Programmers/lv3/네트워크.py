from collections import deque

def solution(n, computers):
    tot = 0
    bfs = deque()
    ch = [0] * n

    while 0 in ch:
        bfs.append(ch.index(0))
        while bfs:
            tmp = bfs.popleft()
            ch[tmp] = 1
            for i in range(n):
                if ch[i] == 0 and computers[tmp][i] == 1:
                    bfs.append(i)
        tot += 1
    return tot

print(solution(	3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))