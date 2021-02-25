def DFS(L,sum,ch):
    global cnt
    if L > len(li):
        return
    if ch == k :
        if sum % m == 0:
            cnt+=1
        return
    elif L == len(li):
        return
    else:
        DFS(L+1,sum+li[L],ch+1)
        DFS(L+1,sum,ch)

if __name__ == "__main__":
    n,k = map(int, input().split())
    li = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0,0,0)
    print(cnt)