n = 2
li = [[0]*n]*n
print(li)
li[0][1]=2
print(li)

print()
li2 = [[0]*n for _ in range(n)]
print(li2)
li2[0][1]=2
print(li2)