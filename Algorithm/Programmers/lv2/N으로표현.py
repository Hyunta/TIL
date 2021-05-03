def solution(N, number):
    answer = -1
    dy = [[]]

    for i in range(1,9):
        case = set()
        m_num = int(str(N)*i) # NN 꼴 더해주기
        case.add(m_num)

        #사칙연산으로 표현된 값 더해주기 총합이 i개가 되도록
        for j in range(1,i):
            for a in dy[j]:
                for b in dy[-j]:
                    case.add(a+b)
                    case.add(a-b)
                    case.add(a*b)
                    if b != 0:
                        case.add(a//b)
        if number in case:
            answer = i
            break
        
        dy.append(case)

    return answer

print(solution(5,12))
print(solution(2,11))