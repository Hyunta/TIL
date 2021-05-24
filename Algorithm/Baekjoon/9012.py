import sys
input = sys.stdin.readline

def check(s):
    li = []
    for i in range(len(tmp)):
        if tmp[i] == '(':
            li.append(tmp[i])
        elif tmp[i] == ')':
            if li:
                li.pop()
            else:
                return 'NO'
    if li:
        return 'NO'
    else:
        return 'YES'

n = int(input())
for _ in range(n):
    tmp = input()
    print(check(tmp))