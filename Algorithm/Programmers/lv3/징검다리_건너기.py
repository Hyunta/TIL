def solution(stones, k):
    lt = 1
    rt = max(stones)
    answer = 0

    while lt <= rt:
        spc = 0

        mid = (lt+rt)//2

        for stone in stones:
            if stone - mid <= 0:
                spc += 1
            else:
                spc = 0
            if spc == k: # 징검다리 간격이 k이상일 경우 불가능
                break

        if spc < k: # mid 이상에서 답이 되는 경우
            lt = mid+1
            answer = mid+1
        else:
            rt = mid -1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))