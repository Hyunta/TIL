def solution(arr):
    answer = [0,0]
    n = len(arr)

    def comp(x,y,n):
        init = arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != init:
                    n2 = n // 2
                    comp(x,y,n2)
                    comp(x+n2,y,n2)
                    comp(x,y+n2,n2)
                    comp(x+n2,y+n2,n2)
                    return
        answer[init] += 1
    comp(0,0,n)
    return answer
        
