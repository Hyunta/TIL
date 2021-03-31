def DFS(L,sum):
    if L == k:
        ch.append(sum)
    else:
        DFS(L+1,sum+li[L])
        DFS(L+1,sum)




if __name__ == "__main__":
    k = int(input())
    li = list(map(int,input().split()))
    s = sum(li)
    ch = []
    DFS(0,0)
    print(ch)
    tot = len(list(set(ch)))
    print(s)
    print(tot)