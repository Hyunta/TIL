def solution(n):
    m = bin(n)[2:]
    for i in range(1,n):
        tmp = bin(n+i)[2:]
        if tmp.count('1') == m.count('1'):
            return n+i