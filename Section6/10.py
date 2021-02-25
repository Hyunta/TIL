#조합구하기

def DFS(L,ch):
    global cnt
    if L > n+1:
        return
    if ch == m:
        for x in res:
            print(x, end=' ')
        cnt +=1
        print()
    else:
        res.append(L)
        DFS(L+1,ch + 1)
        res.remove(L)
        DFS(L+1,ch)

if __name__ == "__main__":
    n,m = map(int, input().split())
    cnt = 0
    res = []
    DFS(1,0)
    print(cnt)