cnt =0
def DFS(v,tot,numbers,target):
    global cnt
    if v < len(numbers):
        DFS(v+1,tot-numbers[v],numbers,target)
        DFS(v+1,tot+numbers[v],numbers,target)
    elif tot == target:
        cnt += 1
    
def solution(numbers, target):
    global cnt
    DFS(0,0,numbers,target)
    print(cnt)

solution([1, 1, 1, 1, 1], 3)