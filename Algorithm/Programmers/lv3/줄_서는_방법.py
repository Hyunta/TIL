from math import factorial as f
def solution(n, k):
    answer = []
    nl = list(range(1,n+1))
    while n!=0 :
        fact = f(n-1)
        answer.append(nl.pop((k-1)//fact))
        n -= 1
        k %= fact
    return answer