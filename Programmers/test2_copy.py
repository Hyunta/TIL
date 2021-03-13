from itertools import combinations
def solution(info, query):
    answer=[]
    db={}
    for x in info:
        tmp = x.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])
        for n in range(5):
            comb = list(combinations(range(4), n))
            for c in comb:
                tmp_con= conditions.copy()
                for v in c:
                    tmp_con[v] = '-'
                changed_tot = '/'.join(tmp_con)
                if changed_tot in db:
                    db[changed_tot].append(score)
                else:
                    db[changed_tot] = [score]

    for v in db.values():
        v.sort()
    
    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_con = '/'.join(qry[:-1])
        qry_scr = int(qry[-1])
        if qry_con in db:
            data = db[qry_con]
            if len(data)>0:
                lt, rt = 0, len(data)
                while lt <rt:
                    mid = (lt+rt)//2
                    if data[mid] >= qry_scr:
                        rt = mid
                    else:
                        lt = mid + 1
                answer.append(len(data)-lt)
        else: 
            answer.append(0)

    return(answer)


 
