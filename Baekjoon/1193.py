n = int(input())
li=[]
i=1

while (i**2-i+2)/2 <= n:
    i+=1

#i-1번쨰 대각라인에 위치
m = int(((i-1)**2-(i-1)+2)/2)
res = n-m

#i-1번째 대각선 시작점과의 차이

if (i-1)%2 == 0: 
    #짝수이면
    print(1+res,i-1-res,sep='/')
else: #홀수이면
    print(i-1-res,1+res, sep='/')