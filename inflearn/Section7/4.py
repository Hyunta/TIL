def DFS(L,sum):
    global cnt
    if sum > t:
        return
    if sum == t:
        cnt +=1
    else:
        if L < k:
            for i in range(m[L][1]+1):
                DFS(L+1,sum+m[L][0]*i)


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    m = list()
    for _ in range(k):
        n,p = map(int, input().split())
        m.append([n,p])
    cnt = 0
    DFS(0,0)
    print(cnt)