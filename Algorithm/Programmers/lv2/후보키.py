from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidate = list()
    for i in range(1, n_col+1):
        candidate.extend(combinations(range(n_col), i))  #종목별로 만들 수 있는 모든 조합갯수 찾기

    final = []
    for keys in candidate:
        tmp = [tuple([item[key] for key in keys]) for item in relation] # 주어진 키로 리스트의 index별 아이템 뽑아내기
        if len(set(tmp)) == n_row: #set로 변경후 사라진게 없다면 key로 사용해도 무방
            final.append(keys)

    print(final)
    answer = set(final[:])
    print("answer", answer)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))): # key 중에 겹치는 부분이 있는 것을 삭제
                answer.discard(final[j])
    return(len(answer))
            

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))