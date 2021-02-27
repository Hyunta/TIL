import sys
def DFS(L,A,B,C):
    global res
    if L == n and A!=B and B!=C and C!=A:
        if res > max(A,B,C)-min(A,B,C):
           # print("A=",A,"B=",B,"C=",C)
            res = max(A,B,C)-min(A,B,C)
           # print("res=",res)
    else:
        if L<n:
            DFS(L+1,A+li[L],B,C)
            DFS(L+1,A,B+li[L],C)
            DFS(L+1,A,B,C+li[L])

if __name__ == "__main__":
    n = int(input())
    li = list(int(input()) for _ in range(n))
    res = sys.maxsize
    DFS(0,0,0,0)
    print(res)