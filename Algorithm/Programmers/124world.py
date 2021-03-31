n = int(input())
world = '124'
a=''
while n > 0 :
    n -= 1
    a = world[n%3] + a
    n = n//3
print(a)

