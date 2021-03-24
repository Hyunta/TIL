'''
n = [int(x) for x in str(input())]
n.sort(reverse=True)
for x in n:
    print(x, end='')

'''
import sys
n = [int(x) for x in str(sys.stdin.readline().rstrip())]
n.sort(reverse=True)
for x in n:
    print(x, end='')
