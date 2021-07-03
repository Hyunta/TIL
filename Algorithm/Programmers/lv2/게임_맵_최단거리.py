from collections import deque

def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    row = len(maps)
    column = len(maps[0])

    ch = [[-1] * column for _ in range(row)]

    q = deque()
    q.append([0,0])
    ch[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < row and 0 <= nx < column and maps[ny][nx] == 1:
                if ch[ny][nx] == -1:
                    ch[ny][nx] = ch[y][x] + 1
                    q.append([nx, ny])

    answer = ch[-1][-1]
    return answer



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1,1,1],[1,1,1]]))