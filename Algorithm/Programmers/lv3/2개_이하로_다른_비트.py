def solution(numbers):
    res = []
    for number in numbers:
        bin_li = list(bin(number)[2:])
        size = len(bin_li)

        if bin_li.count('0') == 0:
            res.append(int(('10'+'1'*(size-1)),2))
        else:
            for i in range(size):
                if bin_li[-i] == '0':
                    bin_li[-i] = '1'
                    break

            for j in range(i-1,0,-1):
                if bin_li[-j] == '1':
                    bin_li[-j] = '0'
                    break
            res.append(int(''.join(bin_li),2))
    return res







print(solution([2, 7]))
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))

