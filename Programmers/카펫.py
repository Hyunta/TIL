def solution(brown, yellow):
    for i in range(1,yellow if yellow != 1 else 2):
        if i*2 + (yellow/i)*2 + 4 == brown:
            return [yellow/i+2,i+2]