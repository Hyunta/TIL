'''
s = list(map(str, input()))
li = [-1]*26
ch = list()
for k,v in enumerate(s):
    if v not in ch:
        li[ord(str(v))-97] = k
        ch.append(v)
for x in li:
    print(x, end=' ')
'''

s = input()
al ='abcdefghijklmnopqrstuvwxyz'

for x in al:
    print(s.find(x), end=' ')