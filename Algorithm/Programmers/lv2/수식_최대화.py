from itertools import permutations

def cal(a,b,n):
    if n == '+':
        return a + b
    elif n == '-':
        return a - b
    elif n == '*':
        return a * b

def solution(expression):
    #기본 설정
    result = 0
    li = []
    tmp = ''
    
    # 주어진 스트링을 리스트(숫자와 기호)로 변환
    for x in expression:
        if x.isnumeric():
            tmp += x
        else:
            li.append(int(tmp))
            li.append(x)
            tmp = ''
    li.append(int(tmp))

    # 연산자 순열을 통해 모든 경우에서의 최댓값 찾기
    operators= ['+','-','*']
    for perm in permutations(operators,3):
        tmp_li = li[:]
        for operator in perm:
            idx = 0
            while idx < len(tmp_li):
                if tmp_li[idx] == operator:
                    tmp_cal = cal(tmp_li[idx-1], tmp_li[idx+1],operator)
                    tmp_li = tmp_li[:idx-1] + [tmp_cal] + tmp_li[idx+2:]
                else:
                    idx += 1
        else:
            result = max(result, abs(int(tmp_li[0])))
    return result

print(solution("100-200*300-500+20"))