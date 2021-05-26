def solution(genres, plays):

    gen_tot = dict()
    res = dict()
    answer = list()
    
    for i in range(len(genres)):
        gen_tot[genres[i]] = gen_tot.get(genres[i], 0) + plays[i]
        res[genres[i]] = res.get(genres[i], []) + [(plays[i],i)]
    
    fin = sorted(gen_tot.items(), key=lambda x: x[1], reverse=True)
    
    for (genre,_) in fin:
        res[genre] = sorted(res[genre], key= lambda x : [-x[0],x[1]])
        answer += [idx for [play, idx] in res[genre][:2]]
    return answer

print(solution(['classic'], [2500]) == [0])