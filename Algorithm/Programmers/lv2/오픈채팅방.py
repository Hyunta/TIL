def solution(record):
    answer=[]
    result = dict()
    record2 = record[::-1]
    for x in record2:
        tmp = list(map(str, x.split()))
        print(tmp)
        if tmp[0] == 'Change' and tmp[1] not in result:
            result[tmp[1]] = tmp[2]
        if tmp[0] == 'Enter' and tmp[1] not in result:
            result[tmp[1]] = tmp[2]
    print(result)
    for y in record:
        tmp = list(map(str, y.split()))
        if tmp[0] == 'Enter':
            if tmp[1] not in result:
                answer.append("{tmp[2]}님이 들어왔습니다.")
            else:
                answer.append("%s님이 들어왔습니다." %(result[tmp[1]]))
        if tmp[0] == 'Leave':
            if tmp[1] not in result:
                answer.append("{tmp[2]}님이 나갔습니다.")
            else:
                answer.append("%s님이 나갔습니다." %(result[tmp[1]]))

    print(answer)




print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))