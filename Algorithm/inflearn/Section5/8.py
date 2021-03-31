n = int(input())
wl=[]
pl=[]
for i in range(n):
    wl.append(input())

for j in range(n-1):
    pl.append(input())

for x in wl:
    if x not in pl:
        print(x)