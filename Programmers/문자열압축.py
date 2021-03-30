from collections import deque
def solution(s):
    res = len(s)
    for i in range(1,len(s)//2+1):
        tmp_q = deque()
        tmp_s = ""
        for j in range(0,len(s),i):
                tmp_q.append(s[j:j+i])
        print(tmp_q)
        tmp_q.append(0)
        cnt = 1
        for i in range(1,len(tmp_q)):
            if tmp_q[i-1] == tmp_q[i]:
                cnt += 1
            else:
                if cnt !=1:
                    tmp_s += str(cnt)
                tmp_s += tmp_q[i-1]
                cnt = 1
        print(tmp_s)
        if len(tmp_s) < res:
            res = len(tmp_s)
    print(res)
        
'''
        if len(tmp_s) < res:
            res = len(tmp_s)
    return res
'''
#solution("aabbaccc")
#solution("ababcdcdababcdcd")
#solution("abcabcdede")
solution("dedeabcabc")
#solution("abcabcabcabcdededededede")
#solution("xababcdcdababcdcd")
#solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#solution("aaaaaaaaaab")
#solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz")
#solution("xxxxxxxxxxyyy")
solution("xxxxxxxxxxyyy")
solution("aababa")
solution("aasaasaas")
solution("fabababab")