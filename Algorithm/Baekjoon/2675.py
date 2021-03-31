t = int(input())
for _ in range(t):
    r,s =map(str, input().split())
    for x in s:
        for i in range(int(r)):
            print(x, end='')
    print()

'''
a=int(input())
for i in range(a):
    c,d=input().split()
    text=''
    for j in d:
        text+=int(c)*j
    print(text)
'''