n=input()
num=[]
for x in n:
    num.append(x)

while len(num)!=1:
    cnt = 0
    for k,v in enumerate(num):
        if str(v).isnumeric():
            cnt += 1
        if cnt >=2 and not str(v).isdecimal():
            a = int(num[k-2])
            b = int(num[k-1])
            if v == '+':
                res = a+b
            elif v == '-':
                res = a-b
            elif v == '*':
                res = a*b
            else:
                res = a/b
            del num[k-2:k+1]
            num.insert(k-2,res)
            break
print(num[0])
                
             
            
