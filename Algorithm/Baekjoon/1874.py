import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
result = []
pos = True

for _ in range(n):
    tmp = int(input())

    while count < tmp:
        count += 1
        stack.append(count)
        result.append('+')

    top = stack[-1]
    if top == tmp:
        stack.pop()
        result.append('-')
    else:
        pos = False
        break

if not pos:
    print('NO')
else:
    for r in result:
        print(r)
