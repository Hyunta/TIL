def rotate90(key):
    return list(zip(*key[::-1]))

def use_key(x,y,m,key,board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]

def undo_key(x,y,m,key,board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]

def check(board,m,n):
    for i in range(n):
        for j in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True

def solution(key, lock):
    m,n = len(key) , len(lock)
    board = [[0]*(m*2 + n) for _ in range(m*2 + n)]
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]

    rot_key = key
    for _ in range(4):
        rot_key = rotate90(rot_key)
        for x in range(1,m+n):
            for y in range(1,m+n):
                use_key(x,y,m,rot_key,board)
                if check(board,m,n):
                    return True
                undo_key(x,y,m,rot_key,board)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))