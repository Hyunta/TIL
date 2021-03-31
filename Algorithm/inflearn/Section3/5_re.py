N, M = map(int, input().split())
num_seq = [int(x) for x in input().split()]

cnt = 0

for k,v in enumerate(num_seq):
    sum = 0
    for i,j in enumerate(num_seq[k:]):
        print(i+k, end=" ")
        sum = num_seq[i+k] + sum
        print(sum)
        if sum == M:
            cnt += 1
            break
        if sum > M:
            break
    print("\n")
print(cnt)   