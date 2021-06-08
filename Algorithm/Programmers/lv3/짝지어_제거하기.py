def solution(s):
    stack = []
    for x in s:
        if stack:
            if x == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)

    if stack:
        return 0
    else:
        return 1

print(solution('baabaa'))