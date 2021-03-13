n,m = map(int, input().split())
li = list(map(int,input().split()))
li.sort()

lt = 0
rt = n-1
while lt < rt:
    mid = (lt +rt)//2
    if m == li[mid]:
        print(mid+1)
        break
    elif m > li[mid]:
        lt = mid +1
    else:
        rt = mid

