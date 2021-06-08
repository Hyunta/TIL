import sys

def Qsort(lt,rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)


n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
Qsort(0,n-1)
for x in arr:
    print(x)
