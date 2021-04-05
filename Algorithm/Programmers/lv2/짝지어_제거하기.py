def solution(s):
    while s:
        res = len(s)
        for i in range(1,len(s)):
            if len(s) == 2 and s[i] == s[i-1]:
                return 1
            if s[i] == s[i-1]:
                s = s[:i-1] + s[i+1:]
                break
        if res == len(s):
            return 0
        

print(solution("baabaa"))
print(solution("cdcd"))