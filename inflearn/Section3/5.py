N, M = map(int, input().split())
num_seq = [int(x) for x in input().split()]

cnt = 0
for k, v in enumerate(num_seq):
    if v == M:
        cnt += 1
        print(k,"here")
        continue
    elif v > M:
        continue
    else:
        for i in range(len(num_seq[k+1:])):
            if v+num_seq[k+i] > M:
                break
            elif v+num_seq[k+i] == M:
                cnt += 1
                print(v+num_seq[k+i])
                print(k,"here")
            else:
                v = v+num_seq[k+i]
                continue
print(cnt)