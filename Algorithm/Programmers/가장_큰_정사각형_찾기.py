def solution(board):
    res = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
            if board[i][j] > res:
                res = board[i][j]
    return max(res ** 2, board[0][0]**2)

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])