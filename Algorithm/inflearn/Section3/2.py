n = str(input())

M=[]
for x in n:
    if x.isnumeric():
        M.append(x)

num=int(s.join(M))
cnt=0
for i in range(1,num+1):
    if num%i == 0:
        cnt += 1
        
print(num)
print(cnt)