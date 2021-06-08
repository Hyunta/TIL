'''
s= list(x for x in input())
if s == [" "]:
    print(0)
else:
    sum=1
    for x in s[1:-1]:
        if x == ' ' :
            sum +=1
    print(sum)
'''
print(input().split())