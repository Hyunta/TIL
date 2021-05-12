def solution(lottos, win_nums):
    res = []
    cnt = 0
    zero = 0
    for n in lottos:
        if n in win_nums:
            cnt += 1
        elif n == 0:
            zero += 1
    return [7-(cnt+zero) if cnt+zero != 0 else 6, (7-cnt) if cnt > 0 else 6]