'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''

N,M = map(int, input().split())

num_list=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        num_list.append(i+j)

count = {}
for num in num_list:
    try:
        count[num] += 1
    except:
        count[num] = 1
result = [k for k in count.keys() if count[k] == max(count.values())]
for i in result:
    print (i, end=' ')