n = input()

s=""
for i in n:
    if i.isnumeric():
        s=s+i
        
num=int(s)
cnt=0
for i in range(1,num+1):
    if num%i == 0:
        cnt += 1
        
print(num)
print(cnt)
