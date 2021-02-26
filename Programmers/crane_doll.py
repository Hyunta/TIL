def solution(board, moves):
    res=[0]
    cnt=0
    for x in moves:
        print("res=",res)
        print("x=",x)
        i=0
        while i < len(board):
            print("i=",i)
            if board[i][x-1] != 0:
                if board[i][x-1] == res[-1]:
                    print("value=",board[i][x-1])
                    res.pop()
                    board[i][x-1] = 0
                    cnt +=2
                    break
                else:
                    res.append(board[i][x-1])
                    board[i][x-1] = 0
                    break
            else:
                i+=1         
    print(cnt)

if __name__ == "__main__":
    a=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    b=[1,5,3,5,1,2,1,4]
    solution(a,b)