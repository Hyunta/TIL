con = input()
n = int(input())


for i in range(n):
    q=""
    m = list(x for x in input())
    for x in m:
        for j in range(len(con)):
            if x == con[j]:
                q += x
    if q == con:
        print("#%d"%(i+1),"YES" )
    else:
        print("#%d"%(i+1),"NO" )