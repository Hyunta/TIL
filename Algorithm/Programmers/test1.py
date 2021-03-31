def solution(s):
    m=list(map(int, s.split()))
    print(m)
    res = list()
    res.append(min(m))
    res.append(" ")
    res.append(max(m))
    answer=''
    for x in res:
        answer += str(x)
    return answer
        
        