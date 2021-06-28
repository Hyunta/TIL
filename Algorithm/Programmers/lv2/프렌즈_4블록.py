def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i]) # 주어진 String 리스트로 변환

    while True:
        remove = list([0]*n for _ in range(m)) # remove 리스트를 만들어서 2x2 블록들 체크하기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    remove[i][j], remove[i+1][j], remove[i][j+1], remove[i+1][j+1] = 1, 1, 1, 1 # 2x2블록 체크
        count = 0
        for i in range(m):
            count += sum(remove[i])
        answer += count # 터진 블록개수 세기
        if count == 0: # 블록 터진게 없으면 중단
            break
        for i in range(m-1,-1,-1): # 아래에서 부터 위로 확인 터진 블록들 위에 있는 블록들 부여하기
            for j in range(n):
                if remove[i][j] == 1:
                    x = i -1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0: # 만약 위에 아무것도 없으면
                        board[i][j] = 0
                    elif remove[x][j] != 1: # 위에 블록이 있으면
                        board[i][j] = board[x][j]
                        board[x][j] = 0
                        remove[x][j] = 1
    return answer



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
