l = int(input())
S = [int(x) for x in input().split()]
m = int(input())

for _ in range(m):
    S.sort(reverse=True)
    S[0] -= 1
    S[l-1] += 1
    
print(max(S)-min(S))

