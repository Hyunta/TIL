def check(val):
    st = list()
    for x in val:
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
    if not st:
        return True
    else:
         return False

def solution(s):
    if len(s) == 1:
        return 0
    cnt = 0
    for i in range(len(s)):
        tmp_s = s[i:]+s[:i]
        if check(tmp_s):
            cnt += 1
    return cnt