info =["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
li=[]
con=[]
for x in info:
    a = list(map(str, x.split()))
    li.append(a)

for y in query:
    b = list(map(str, y.split()))
    con.append(b)

res=[]
for z in con:
    cnt =0
    for x in li:
        print(z)
        print(x)
        if (z[0] == x[0] or z[0] == '-') and (z[2] == x[1] or z[2] == '-') and (z[4] == x[2] or z[4] == '-') and (z[6] == x[3] or z[6] == '-') and int(z[7]) <= int(x[4]):
            cnt +=1
    res.append(cnt)
return(res)
 
