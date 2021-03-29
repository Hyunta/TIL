def solution(skill, skill_trees):
    cnt = 0
    for x in skill_trees:
        tmp=[]
        for i in x:
            if i in skill:
                tmp.append(i)
        if all(tmp[j] == skill[j] for j in range(len(tmp))):
                cnt += 1
    return cnt