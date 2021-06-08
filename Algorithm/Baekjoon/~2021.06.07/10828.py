import sys
input = sys.stdin.readline
n = int(input())
s = list()
for i in range(n):
    tmp = input().split()
    if tmp[0] == 'push':
        s.append(tmp[1])
    elif tmp[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(s))
    elif tmp[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)