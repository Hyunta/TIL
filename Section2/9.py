N = int(input())

result=[]
for n in range(N):
    M = [int(x) for x in input().split()]
    if M[0] == M[1]:
        if M[1] == M[2]:
            result.append(10000+M[0]*1000)
        elif M[1] != M[2]:
            result.append(1000+max(M)*100)
    elif M[0] != M[1]:
        if M[1] == M[2]:
            result.append(1000+max(M)*100)
        elif M[1] != M[2]:
            if M[2] == M[0]:
                result.append(1000+max(M)*100)
            elif M[2] != M[0]:
                result.append(max(M)*3)
print(max(result))

            
