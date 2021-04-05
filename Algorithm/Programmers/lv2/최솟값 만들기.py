def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    res=0
    for i in range(len(A)):
        res += A[i]*B[i]
    return res