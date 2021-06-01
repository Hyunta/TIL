def solution(triangle):
    d = triangle[:]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                d[i][j]+=d[i-1][j]
            elif i ==j:
                d[i][j] += d[i-1][j-1]
            else:
                d[i][j] += max(d[i-1][j-1], d[i-1][j])
    answer = max(d[-1])
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))