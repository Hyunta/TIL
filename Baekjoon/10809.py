
s = list(map(str, input()))
li = [-1]*26
ch = list()
for k,v in enumerate(s):
    if v not in ch:
        li[ord(str(v))-97] = k
        ch.append(v)
for x in li:
    print(x, end=' ')