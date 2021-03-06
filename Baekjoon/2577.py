a = int(input())
b = int(input())
c = int(input())

res = a*b*c

li =  [0]*10

for i in str(res):
    li[int(i)] += 1

for x in li:
    print(x)