from collections import deque
def check(place):
    ch = [[0]*5 for _ in range(5)]
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                q = deque()
                q.append((i,j,0))
                ch[i][j] = 1
                while q:
                    print(q)
                    tmp = q.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        z = tmp[2] + 1
                        if 0<= x < 5 and 0 <= y < 5 and z <=2 and ch[x][y] == 0:
                            if place[x][y] == 'O':
                                q.append((x,y,z))
                                ch[x][y] = 1
                            elif place[x][y] == 'P':
                                return False
    return True
                        
                    
                    
def solution(places):
    res= []
    for place in places:
        print("----------------------")
        if check(place):
            res.append(1)
        else:
            res.append(0)              
    return res

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))