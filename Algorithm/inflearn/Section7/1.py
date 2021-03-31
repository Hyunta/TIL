# 최대점수 구하기(DFS)

def DFS(L,sum,t):
    global res
    if t > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+li[L][0],t+li[L][1])
        DFS(L+1,sum,t)

n,m = map(int, input().split())
li=[]
for i in range(n):
    x,y = map(int, input().split())
    li.append((x,y))
res = 0
DFS(0,0,0)
print(res)