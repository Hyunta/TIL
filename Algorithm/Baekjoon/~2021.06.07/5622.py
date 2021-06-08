dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()
res = 0
for j in range(len(s)):
    for piece in dial:
        if s[j] in piece:
            res += dial.index(piece)+3
print(res)