n = int(input())
i= 0
if n == 1:
    print(1)
else:
    while n >= 3*i**2-3*i+2:
        i+=1
    print(i)