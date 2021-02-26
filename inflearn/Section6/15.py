def DFS(L):
    global cnt
    if L == n-1:
        cnt += 1
        for x in path:
            print(x+1, end= ' ')
        print()
    else:
        for i in range(n):
            if s[L][i] == 1 and res[L] == 1:
                res[L] = 0
                path.append(i)
                DFS(i)
                path.pop()
                res[L] = 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = list([0 for _ in range(n)] for _ in range(n))
    res = [1]*n
    cnt = 0
    path=[0]
    for _ in range(m):
        x,y = map(int, input().split())
        s[x-1][y-1] = 1
    DFS(0)
    print(cnt)
    