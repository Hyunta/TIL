import sys
input = sys.stdin.readline

def bin_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid -1
    return 0

n = int(input())
li1 = sorted(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

for x in range(m):
    print(bin_search(li1, li2[x]))