import sys

def solution(ages, wires):
    gen = len(ages)
    graph = [[0] * gen for _ in range(gen)]
    result = []

    for wire in wires:
        i,j,val = wire
        graph[i-1][j-1] = val

    time = []
    for i in range(len(ages)):
        time.append([i,ages[i]])

    time.sort(key=lambda x: [x[1],x[0]])

    days = min(ages)

    # while sum(list(x for y in time[x][1]):
    #     res = 100000000
    #     for i in range(len(time)):
    #         time[i][1] -= days
    #         if time[i][1] < 0:
    #             time[i][1] = 0
    #         if time[i][1] < res and time[i][1] > 0:
    #             res = time[i][1]
    #     days = res
    #     print(time)

print(solution([35,25,3,8,7], [[1,2,5],[2,1,5],[1,3,2],[3,4,2],[3,5,20],[4,5,1]]))