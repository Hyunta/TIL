'''
n = int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
li.sort()
for x in li:
    print(x)
'''

import sys
n = int(sys.stdin.readline())
li=[]
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
for x in li:
    print(x)