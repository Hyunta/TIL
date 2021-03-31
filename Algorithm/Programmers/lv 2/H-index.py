def solution(citations):
    citations.sort()
    h=0
    for i in range(len(citations)):
        for j in range(citations[i]+1):
            if j <= len(citations[i:]):
                if h < j:
                    h = j
    return h