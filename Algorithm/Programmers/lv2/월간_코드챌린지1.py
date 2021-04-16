def check(val):
    st = list()
    for x in val:
        print("st=", st)
        if x == "[" or x == "(" or x == "{":
            st.append(x)
        else:
            if not st:
                return False
            if x == "]":
                if st.pop() != "[":
                    return False
            elif x == ")":
                if st.pop() != "(":
                    return False
            elif x == "}":
                if st.pop() != "{":
                    return False
    return True
print(check("[](){}"))


def solution(s):
    cnt = 0
    for i in range(len(s)):
        tmp_s = s[i:]+s[:i]
        print("tmp_s=",tmp_s)
        if check(tmp_s):
            print(tmp_s, "pass")
            cnt += 1
    return cnt

print(solution("[](){}"))
