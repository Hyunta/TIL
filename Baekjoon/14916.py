n, m = map(int, input().split())
al =['A','B','C','D','E','F']
a=''
if n == 0:
    print(0)
    exit(0)
while n > 0:
    if n%m > 9:
        a = al[(n%m)%10] + a
    else:
        a = str(n%m) + a
    n = n // m
print(a) 