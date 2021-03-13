info =["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import combinations
def solution(info, query):
    db={}
    answer=[]
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
                while lt != rt and lt != len(data):
                    if data[(lt+rt)//2] >= qry_scr:
                        rt = (lt+rt)//2
                    else:
                        lt = (lt+rt)//2 + 1
                answer.append(len(data)-lt)
            else: 
                answer.append(0)
    return(answer)
        
solution(info,query)

 
