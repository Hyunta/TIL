def solution(n, k):
    global c
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    c = 1
    def DFS(L):
        global cnt
        global c
        if L == n:
            c += 1
            if c == k:
                return res
        else:
            for i in range(1,n+1):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    DFS(L+1)
                    ch[i] = 0    
    DFS(0)

print(solution(3,5))