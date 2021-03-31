a = input()
b = input()
c = dict()

for x in str(a):
    if x in c:
        c[x] += 1
    else:
        c[x] = 1

for x in str(b):
    if x in c:
        c[x] -= 1
    else:
        c[x] = 1

if any(v != 0 for v in c.values()):
    print("NO")
else:
    print("YES")
