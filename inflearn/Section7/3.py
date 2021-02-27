def DFS(L,lsum,rsum):
    if 1<= abs(lsum-rsum)<=s:
        ch.append(abs(lsum-rsum))
    if L >= k:
        return
    else:   
        DFS(L+1,lsum+li[L],rsum)
        DFS(L+1,lsum,rsum)
        DFS(L+1,lsum,rsum+li[L])




if __name__ == "__main__":
    k = int(input())
    li = list(map(int,input().split()))
    s = sum(li)
    ch = []
    DFS(0,0,0)
    tot = len(list(set(ch)))
    print(s-tot)
