a,b,c = map(int, input().split())
cost = a
income = 0
x=0
if b>=c:
    x= -1
else:
    x = a//(c-b)+1
print(x)