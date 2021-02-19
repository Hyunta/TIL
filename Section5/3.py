n = input()
stack =[]
res = ''

for x in n:
    if x.isdecimal():#숫자인지 확인하는 함수 () 써야함
        res += x
    else:
        if x == '(': # append 안시키면 ( 나왔을 때 else 계산으로 가버림
            stack.append(x)
        elif x == ')': # 괄호가 닫히면 괄호안의 기호 계산
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        elif x == '*' or x =='/': # x,/는 +,- 빼고 모두출력
            if stack: # 스택이 비었을 경우 리스트 인덱스 범위를 벗어남
                while stack[-1] == '*' or stack[-1] =='/':
                    res += stack.pop()
            stack.append(x)
        elif x == '+' or x =='-':
            while stack and stack[-1] != '(': # +,-를 만나면 모두다 출력
                res += stack.pop()
            stack.append(x)
while stack:
    res += stack.pop()
print(res)



'''
for i in range(len(n)):
    print(i)
    if len(n) == 0: #끝나면 남은 기호를 전부 s 에 추가
        while len(tmp)==0:
            s += tmp.pop()
    if n[i] in opr:  # 기호 or 괄호이면
        tmp.append(n[i])
        if n[i] == ')':
            tmp.pop()
            while tmp[-1] == '(':
                s += tmp.pop()
                tmp.pop()
        if n[i] == '*' or n[i] == '/':
            continue
        elif n[i] == '+' or n[i] =='-':
            while tmp[-1] != '*' or tmp !='/':
                s += tmp.pop()
    else:  # 숫자면
        s += n[i]
'''