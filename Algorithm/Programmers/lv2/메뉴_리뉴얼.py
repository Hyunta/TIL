from itertools import combinations
def solution(orders, course):
    res = []
    for i in course:
        d = dict()
        for order in orders:
            for comb in list(combinations(sorted(order),i)):
                tmp_str=''
                for j in range(len(comb)):
                    tmp_str += comb[j]
                d[tmp_str] = d.get(tmp_str, 0)+1
        for x in d:
            if max(d.values()) > 1 :
                if d[x] == max(d.values()):
                    res.append(x)
    return sorted(res)



print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
