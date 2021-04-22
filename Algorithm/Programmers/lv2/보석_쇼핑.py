def solution(gems):
    tot = len(set(gems))
    d = {gems[0]:1}
    res = [0,len(gems)-1]
    lt,rt = 0, 0
    while lt < len(gems) and rt < len(gems):
        if len(d) == tot:
            if rt - lt < res[1] - res[0] :
                res =[lt,rt]
            if d[gems[lt]] == 1:
                del(d[gems[lt]])
            else:
                d[gems[lt]] -= 1
            lt += 1
        else:
            rt += 1
            if rt == len(gems):
                break
            d[gems[rt]] = d.get(gems[rt],0) + 1
    return [res[0]+1, res[1]+1]



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))