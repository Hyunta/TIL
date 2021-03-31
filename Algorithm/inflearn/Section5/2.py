m = input()
stack=[]
sum=0

for i in range(len(m)):
    if m[i] == '(':
        stack.append(m[i])
    else:
        stack.pop()
        if m[i-1] == '(': #레이저
            sum += len(stack)
        else: # 끄트머리
            sum += 1

print(sum)