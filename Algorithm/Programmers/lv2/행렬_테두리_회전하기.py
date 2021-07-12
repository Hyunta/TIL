def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]

    num = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i - 1].append(num)
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = board[x1 - 1][y1 - 1]
        mini = tmp

        for k in range(x1 - 1, x2 - 1):
            test = board[k + 1][y1 - 1]
            board[k][y1 - 1] = test
            mini = min(mini, test)

        for k in range(y1 - 1, y2 - 1):
            test = board[x2 - 1][k + 1]
            board[x2 - 1][k] = test
            mini = min(mini, test)
        
        for k in range(x2-1, x1-1, -1):
            test = board[k-1][y2-1]
            board[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1, y1-1, -1):
            test = board[x1-1][k-1]
            board[x1-1][k] = test
            mini = min(mini, test)

        board[x1-1][y1] = tmp
        answer.append(mini)

    return answer