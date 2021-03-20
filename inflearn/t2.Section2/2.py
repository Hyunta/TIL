t = int(input())
for i in range(t):
    n,s,e,k = map(int, input().split())
    li = list(map(int, input().split()))
    li2 = li[s-1:e]
    li2.sort()
    print("#%d"%(i+1),li2[k-1])
