n = int(input())

for _ in range(n):
    m = list(x for x in input())
    cnt = 0
    sum = 0
    for x in m:
        if x == 'O':
            cnt += 1
            sum += cnt
        if x == 'X':
            cnt = 0
    print(sum)