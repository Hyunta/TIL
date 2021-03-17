def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    li = ["-",'_','.']
    for x in str(new_id):
        if not x.isalnum() and x not in li :
            new_id = new_id.replace(x,'')
    #3단계
    res = ["0"]
    for i in range(len(new_id)):
        if res[-1] =='.' and new_id[i]=='.':
            continue        
        else:
            res.append(new_id[i])
    res.pop(0)
    #4단계
    print("res=",res)
    if res:
        if res[0] == '.':
            res.pop(0)
        if res and res[-1] == '.':
            res.pop()
        new_id =""
        for x in res:
            new_id += x
    else:
        new_id = ""
    print("res_after4=",res)
    #5단계
    if new_id == "":
        new_id+="a"
    
    #6단계
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:14]
    
    #7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id