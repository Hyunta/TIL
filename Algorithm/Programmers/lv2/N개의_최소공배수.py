def solution(arr):
    arr.sort(reverse=True)
    var = 1
    while True:
        ch = 0
        tmp = arr[0] * var
        for x in arr[1:]:
            if tmp % x != 0:
                ch = 1
                break
        if ch == 0:
            return tmp
        var += 1
print(solution([1,2,3]))