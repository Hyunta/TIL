def solution(numbers):
    ch = []
    for number in numbers:
        tmp = ''
        for i in range(len(str(number))):
            tmp += changeNum(str(number)[i])
        ch.append((tmp,len(ch)))
    ch.sort()

    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[ch[i][1]])
    return answer


def changeNum(number):
    li = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    return li[int(number)]

print(solution([6,1,8]))
print(solution([4,5,11]))