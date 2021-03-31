def solution(s, n):
    # A=65,Z=90
    # a=97,z=122
    a=''
    for x in s:
        if x == ' ':
            a += x
        elif 64<ord(x)<91:
            if ord(x)+n > 90:
                a+= chr(ord(x)+n-26)
            else:
                a+=chr(ord(x)+n)
        else:
            if ord(x)+n > 122:
                a += chr(ord(x)+n-26)
            else:
                a += chr(ord(x)+n)
    return a