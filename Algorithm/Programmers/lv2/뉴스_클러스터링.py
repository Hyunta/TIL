def solution(str1, str2):
    li1, li2 = list(), list()
    
    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            li1.append(str1[i:i+2].lower())
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            li2.append(str2[i:i+2].lower())
            
    union, inter = 0,0
    for s in set(li1+li2):
        union += max(li1.count(s), li2.count(s))
        inter += min(li1.count(s), li2.count(s))
        
    if union == 0:
        return 65536
    else:
        return int(inter/union * 65536)