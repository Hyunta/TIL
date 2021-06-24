def solution(relation):
    n=len(relation[0])
    for i in range(n):
        tmp = []
        for r in relation:
            if r[i] in tmp:
                break
            



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))