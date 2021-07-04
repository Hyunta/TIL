def solution(compressed):
    li = convert(compressed)
    stack = []
    for x in li:
        if x.isnumeric():
            stack.append(x)
        elif x.isalpha():
            if stack[-1].isalpha():
                stack[-1] = stack[-1] + x
            else:
                stack.append(x)
        elif x == ')':
            word = stack.pop()
            cnt = stack.pop()
            if stack and stack[-1].isalpha():
                stack[-1] = stack[-1] + word*int(cnt)
            else:
                stack.append(word*int(cnt))
    return stack[0]



def convert(compressed):
    li = []
    num = ''
    word = ''
    for i in range(len(compressed)):
        x = compressed[i]

        if x.isnumeric():
            if word != '':
                li.append(word)
                word = ''
            num += x

        elif x == '(':
            li.append(num)
            num = ''
            li.append('(')

        elif x.isalpha():
            word += x

        elif x == ')':
            li.append(word)
            word = ''
            li.append(')')

    return li


print(solution("3(hi)"))
print(solution("2(3(hi)co)"))
print(solution("10(p)"))
print(solution("2(2(hi)2(co))x2(bo)"))
print(solution("2(3(hi)2(co))"))