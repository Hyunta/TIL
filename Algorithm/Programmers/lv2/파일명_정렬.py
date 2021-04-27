def solution(files):
    d = dict()
    for f in files:
        head_idx, number_idx = None, None
        for i in range(len(f)):
            if f[i].isnumeric():
                break
            else:
                head_idx = i
        for j in range(head_idx+1, len(f)):
            if f[j].isnumeric():
                number_idx = j
            else:
                break
        head = f[:head_idx+1].lower() 
        number = int(f[head_idx+1:number_idx+1])
        d[f] = (head,number)
    res = list(a for a,b in sorted(d.items(), key=lambda x: (x[1][0], x[1][1])))
    return res


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
        
                