def checknum(n):
    if n == 'zero':
        return 0
    elif n == 'one':
        return 1
    elif n == 'two':
        return 2
    elif n == 'three':
        return 3
    elif n == 'four':
        return 4
    elif n == 'five':
        return 5
    elif n == 'six':
        return 6
    elif n == 'seven':
        return 7
    elif n == 'eight':
        return 8
    elif n == 'nine':
        return 9
    else:
        return 'a'
    
def solution(s):
    answer=[]
    tmp = -1
    res= ''
    for i in range(len(s)):
        if s[i].isnumeric():
            if tmp != -1:
                answer.append(s[tmp:i])
                tmp = -1
            answer.append(s[i])
        else:
            if tmp == -1:
                tmp = i
    if tmp != -1:
        answer.append(s[tmp:])
    for j in range(len(answer)):
        if 1< len(answer[j]) < 6 :
            answer[j] = checknum(answer[j])
        elif len(answer[j]) >= 6:
            tmp_p = 0
            tmp_val = ''
            for k in range(len(answer[j])):
                if str(checknum(answer[j][tmp_p:k+1])).isnumeric():
                    tmp_val += str(checknum(answer[j][tmp_p:k+1]))
                    tmp_p = k+1
            answer[j] = tmp_val
    for y in answer:
        res += str(y)
    return int(res)