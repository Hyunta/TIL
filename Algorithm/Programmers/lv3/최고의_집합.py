def solution(n, s):
    res = [s//n]*n
    if n > s:
        return [-1]
    for i in range(s%n):
        res[-i-1] += 1
    return res