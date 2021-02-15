M = [list(map(int, input().split())) for _ in range(7)]


def check(M):
    if M == M[::-1]:
        return True
    else:
        return False

cnt = 0
for i in range(7):
    for j in range(3):
        if check(M[i][j:j+5]):
            cnt += 1

Sero = []
for j in range(7):
    Ms = []
    for i in range(7):
        Ms.append(M[i][j])
    Sero.append(Ms)

for i in range(7):
    for j in range(3):
        if check(Sero[i][j:j+5]):
            cnt += 1

print(cnt)
