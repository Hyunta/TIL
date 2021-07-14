def solution(line1, line2):
    result = 0

    for n in range(len(line1)+1):
        for i in range(len(line1)):
            if line1[i] == line2[0]:
                pos = i
                for j in range(1,len(line2)):
                    pos += n
                    if pos >= len(line1):
                        break
                    if line1[pos] != line2[j]:
                        break
                else:
                    if pos < len(line1):
                        result += 1
    return result

print(solution("abbbcbbb", "bbb"))