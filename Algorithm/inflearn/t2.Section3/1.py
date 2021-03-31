#회문 문자열 검사
n = int(input())
for i in range(1,n+1):
    tmp = str(input()).lower()
    if tmp == tmp[::-1]:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")
