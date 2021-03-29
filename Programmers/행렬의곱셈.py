'''
def solution(arr1, arr2):
    n=len(arr1)
    m=len(arr2[0])
    res=list([0]*m for _ in range(n))
    for i in range(n):
        for j in range(m):
            for k in range(len(arr2)):
                res[i][j] += arr1[i][k]*arr2[k][j]
    print(res)
'''

def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]] )
solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]] )
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]])

