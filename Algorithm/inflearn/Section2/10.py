N = int(input())
M=[int(x) for x in input().split()]

bonus_score=0
result=0
for m in M:
    if m == 0:
        bonus_score = 0
    elif m != 0:
        bonus_score += 1
        result = result + bonus_score
print(result)
    