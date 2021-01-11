'''
변수명 정하기
    1) 영문과 숫자, _ 로 이루어진다.
    2) 대소문자를 구분한다.
    3) 문자나, _ 로 시작한다.
    4) 특수문자를 사용하면 안된다.
    5) 키워드를 사용하면 안된다.
'''

a = 1
A = 2
b = 4
#B=4
print(a, A,b)

#값 교환
a, b = 10, 20
print(a,b)
a,b = b,a
print(a,b)

#변수 타입
a = 123124124124124
print(type(a))
a = 12.1234
print(type(a))
a = "student"
print(a)

#출력방식
print("number")
a, b, c =1, 2, 3
print("number :", a, b, c,)
print(a,b,c,sep=',')
print(a,b,c, sep='\n')
print(a, end = ' ')
print(b, end = ' ')
print(c)
