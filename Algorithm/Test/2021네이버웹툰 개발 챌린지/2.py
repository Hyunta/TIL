def solution(compressed):
    stack = []
    num = ''
    word = ''
    answer = ''
    for i in range(len(compressed)):

        x = compressed[i]

        if x.isnumeric():
            if word != '':
                answer += word
                word = ''
            num += x

        elif x == '(':
            stack.append(int(num))
            num = ''

        elif x.isalpha():
            word += x

        elif x == ')':
            print(stack)
            print(word)
            cnt = stack.pop()
            word = cnt*word

    if word:
        answer += word
    return answer



print(solution("3(hi)"))
print(solution("2(3(hi)co)"))
print(solution("10(p)"))
print(solution("2(2(hi)2(co))x2(bo)"))