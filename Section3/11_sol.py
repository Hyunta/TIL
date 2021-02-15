M = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        tmp = M[i][j:j+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if M[j+k][i] != M[j+5-k-1][i]:
                break
        else:
            cnt+=1
print(cnt)