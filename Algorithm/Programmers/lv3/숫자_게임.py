def solution(A, B):
    srt_a = sorted(A, reverse=True)
    srt_b = sorted(B,reverse=True)
    res = 0
    while srt_b:
        if srt_a[-1] < srt_b[-1]:
            srt_a.pop()
            res += 1
        srt_b.pop()
    return res