import sys
input = sys.stdin.readline

for _ in range(3):
    li = list(map(int, input().split()))
    tmp = sum(li)
    if tmp == 4:
        print('E')
    elif tmp == 3:
        print('A')
    elif tmp == 2:
        print('B')
    elif tmp == 1:
        print('C')
    elif tmp == 0:
        print('D')
