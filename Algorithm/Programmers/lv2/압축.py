def solution(msg):
    answer = []
    d = {}

    for i in range(26):
        d[chr(65+i)] = i+1

    w,c = 0,0
    while True:
        c += 1
        if c == len(msg):
            answer.append(d[msg[w:c]])
            break
        if msg[w:c+1] not in d:
            d[msg[w:c+1]] = len(d) + 1
            answer.append(d[msg[w:c]])
            w = c

    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))