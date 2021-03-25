n = input()
a=""
for x in n:
    if x.isdigit():
        a += x
a = int(a)

cnt=0
for i in range(1,a+1):
    if a%i == 0:
        cnt +=1
print(a)
print(cnt)
