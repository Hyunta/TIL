import sys
def DFS(v):
    if v == n+1:
        A=[]
        B=[]
        for i in range(n):
            if cnt[i] == 1:
                A.append(m[i])
            else:
                B.append(m[i])
        if sum(A) == sum(B):
            print("YES")
            sys.exit(0)
    else:
        cnt[v] = 1
        DFS(v+1)
        cnt[v] = 0
        DFS(v+1)
    


if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    cnt = [0]*(n+1)
    DFS(1)
    print("NO")