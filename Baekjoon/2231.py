n = int(input())

for i in range(max(1,n-54),n):
    tmp = 0
    for z in str(i):
        tmp += int(z)
    if tmp + i == n:
        print(i)
        exit(0)
print(0)
