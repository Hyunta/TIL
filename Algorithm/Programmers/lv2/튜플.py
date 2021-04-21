'''
def solution(s):
    res = dict()
    ans = list()
    tmp_x = ''
    for x in s:
        if x.isnumeric():
            tmp_x += x
        else:
            res[tmp_x] = res.get(tmp_x,0) + 1
            tmp_x = ''
    del(res[''])
    start = int(max(res.values()))
    while start != 0:
        for a,b in res.items():
            if b == start:
                ans.append(int(a))
                start -= 1                
    return ans
'''
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    print("s1=",s1)

    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    

    new_s.sort(key = len)
    print("new_s=",new_s)
    
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
            




print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution(	"{{20,111},{111}}"))