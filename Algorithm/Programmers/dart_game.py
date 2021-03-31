def solution(dartResult):
    res=[]
    tool=[]
    for i in range(len(dartResult)):
        x = dartResult[i]
        if x.isdigit():
            if x == '1' and dartResult[i+1] == '0':
                res.append(10)
            elif x == '0':
                continue
            else:
                res.append(x)
        else:
            tool.append(x)
    cnt=0
    for i in range(len(tool)):
        j=i-cnt
        if tool[i] == 'S':
            res[j] = int(res[j])
        elif tool[i] == 'D':
            res[j] = int(res[j])**2
        elif tool[i] == 'T':
            res[j] = int(res[j])**3
        elif tool[i] == '*':
            if j>0:
                res[j-1] = int(res[j-1])*2
                res[j-2]= int(res[j-2])*2
                cnt += 1
            else: 
                res[j] = int(res[j])*2
                cnt +=1
        elif tool[i] == '#':
            res[j] = -int(res[j])
            cnt += 1
            
    print(res,tool)

solution('1D#2S*3S')