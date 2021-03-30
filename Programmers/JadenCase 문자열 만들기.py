def solution(s):
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            s = s[:i]+s[i].upper()+s[i+1:]
        else:
            s = s[:i]+s[i].lower()+s[i+1:]
    return s