'''
K번째 큰 수
N장의 카드, 같은 숫자 여러장 가능
이중 3장을 뽑아 더하기, 모든 경우의 수,
기록한 값 중 K번째로 큰 수를 출력
'''

N, K = map(int, input().split())
M = [int(x) for x in input().split()]
result=[]
for n1 in range(N):
    for n2 in range(n1+1,N):
        for n3 in range(n2+1,N):
            m = M[n1]+M[n2]+M[n3]
            result.append(m)

result = list(set(result))
print(sorted(result,reverse=True)[K-1])