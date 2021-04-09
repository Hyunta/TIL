def solution(name):
    tot = 0
    for x in name:
        if ord(f"{x}") > ord("N"):
            tot += 26 - (ord(f"{x}") - ord("A"))
        else:
            tot += ord("%s"%(x)) - ord("A")
    i = 0
    j = 0
    cnt1 = 0
    cnt2 = 0
    while True:
        i += 1
        if name[i] == "A":
            cnt1 += 1
        else:
            break
    while True:
        j -= 1
        if name[j] == "A":
            cnt2 += 1
        else:
            break
    tot += len(name) - max(cnt2,cnt1) - 1
    return tot

print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11