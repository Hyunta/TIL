'''
이분검색
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.
'''

N,M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

'''
이분검색을 사용하지 않은 풀이
for k,v in enumerate(li):
    if v == M:
        print(k+1)
'''
lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt)//2
    if M == li[mid]:
        print(mid+1)
        break
    elif M < li[mid] :
        rt = mid-1
    else:
        lt = mid+1