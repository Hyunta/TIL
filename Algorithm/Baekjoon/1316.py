n = int(input())
res = str(1)
err = 0
for _ in range(n):
    m = str(input())
    li = []
    for i in range(len(m)):
        if m[i] in li and m[i-1] != m[i]:
            err += 1
            break
        else:
            li.append(m[i])
print(n-err)