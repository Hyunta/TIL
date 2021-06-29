def solution(n, t, m, p):
    sol = '0'
    tube = ''
    i = 1
    while len(sol) < (t * (m+1)):
        sol += convert(i, n)
        i += 1
    for i in range(t):
        tube += sol[(p-1)+(m*i)]
    return tube


def convert(i, n): # 10진수를 n진수로 변환
    lett = ["A", "B", "C", "D", "E", "F"]
    rev_base = ''

    while i > 0:
        i, mod = divmod(i, n)
        if mod > 9:
            rev_base += lett[mod%10]
        else:
            rev_base += str(mod)

    return rev_base[::-1]

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
