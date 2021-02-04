N = int(input())

M = []
for k in range(2, N+1):
    t = 0
    for i in range(2, k):
        if k % i == 0:
            t += 1
            break
    if t == 0:
        M.append(k)

print(len(M))
