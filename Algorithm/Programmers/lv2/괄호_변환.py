# 문자열 w를 u, v로 분리하는 함수
def divide(w):
    s = 0
    e = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            s += 1
        elif w[i] == ')':
            e += 1
        if s == e:
            return w[:i + 1], w[i + 1:]

def check(v):
    st = []
    for a in v:
        if a == '(':
            st.append(a)
        else:
            if st:
                st.pop()
            else:
                return False
    if not st:
        return True
    else:
        return False

def solution(w):
    if not w:
        return ''

    u,v  = divide(w)

    if check(u):
        return u + solution(v)
    else:
        ans = '('
        ans += solution(v)
        ans += ')'
        for x in u[1:-1]:
            if x == '(':
                ans += ')'
            elif x == ')':
                ans += '('
        return ans    