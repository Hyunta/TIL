def DFS(case):
    if dy[case]>0:
        return dy[case]
    if case == 1 or case == 2:
        return case
    else:
        dy[case]=DFS(case-1)+DFS(case-2)
        return dy[case]
        



if __name__ == "__main__":
    n = int(input())
    dy =[0]*(n+1)
    print(DFS(n))