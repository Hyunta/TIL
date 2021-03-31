n = int(input())
score = list(map(int, input().split()))
avg = round((sum(score)+1)/n)

min_diff = 214000000
min_key = -1

for k,v in enumerate(score):
    tmp = abs(v - avg)
    if tmp < min_diff:
        min_diff = tmp
        min_key = k
    elif tmp == min_diff:
        if v > score[min_key]:
            min_key = k

print(avg, min_key+1)

