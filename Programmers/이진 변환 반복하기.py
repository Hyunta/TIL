def solution(s):
    zero_cnt = 0
    cnt=0
    while len(s) != 1:
        zero_cnt += s.count('0')
        tmp=s.count('1')
        s = bin(tmp)[2:]
        cnt += 1
    return [cnt,zero_cnt]