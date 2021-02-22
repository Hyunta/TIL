#이진트리 순회

def DFS(v):
    if v>15:
        return
    else:
        print(v, end = ' ')
        DFS(v*2)
        DFS(v*2+1)


if __name__ == "__main__":
    DFS(1)