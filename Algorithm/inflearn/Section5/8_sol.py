n=int(input())
p=dict()
for i in range(n):
    word = input()
    p[word]=1
for i in range(n-1):
    word = input()
    p[word] = 0
for k,v in p:
    if v==1:
        print(k)
        break