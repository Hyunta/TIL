'''
리스트와 내장함수(1)
'''

import random as r
b=list()
#print(b)

a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c=a+b
#print(c)

print(a)
a.append(6)
print(a)

a.insert(3,7)
print(a)

a.pop()
print(a)
a.pop(3)
print(a)

a.remove(4)
print(a)

print(a.index(5))

a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(a)) #max 와 min은 인자값에서 최대,최소를 구해준다.
print(a)
r.shuffle(a)
print(a)
a.sort(reverse=True)
print(a)
a.sort()
print(a)
a.clear()
print(a)




