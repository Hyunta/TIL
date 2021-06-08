import sys
input = sys.stdin.readline

k = int(input())
st = list()
for i in range(k):
    tmp = int(input())
    if tmp == 0:
        st.pop()
    else:
        st.append(tmp)
print(sum(st))