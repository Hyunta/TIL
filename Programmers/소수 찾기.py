from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True
        
def solution(numbers):
    num_case = []
    cnt = 0
    for i in range(1,len(numbers)+1):
        tmp = permutations(numbers,i)
        for n in tmp:
            tmp_str = "".join(n)
            num_case.append(int(tmp_str))
    num_case=list(set(num_case))
    for num in num_case:
        if check(num):
            cnt += 1
    return cnt
    