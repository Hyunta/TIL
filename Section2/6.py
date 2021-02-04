'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요
'''

N = int(input())
M = [int(x) for x in input().split()]

def digit_sum(x):
    return sum([int(i) for i in str(x) ])

M_ds=[]
for m in M:
    M_ds.append(digit_sum(m))

k=M_ds.index(max(M_ds))
print(M[k])