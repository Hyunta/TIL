import sys

def DFS(L,sum):
    global last
    if L > last:
        return
    if sum > tp:
        return
    if sum == tp:
        if L < last:
            last = L
    else:
        for x in m:
            DFS(L+1,sum+x)
            print("L=",L+1,"sum=",sum)



if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    m.sort(reverse=True)
    last = sys.maxsize
    tp = int(input())
    DFS(0,0)
    print(last)