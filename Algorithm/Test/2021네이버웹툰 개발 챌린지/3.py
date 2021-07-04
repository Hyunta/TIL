from collections import deque

def solution(play_list, listen_time):
    tot = deque()
    ch = deque()
    res = 0
    for i in range(len(play_list)):
        for _ in range(play_list[i]):
            tot.append(i)


    while listen_time > len(tot):
        tot += tot
    tot += tot

    while tot:
        tmp = tot.popleft()
        if len(ch) < listen_time:
            ch.append(tmp)
        elif len(ch) == listen_time:
            ch.popleft()
            ch.append(tmp)
            if len(set(ch)) >= res:
                res = len(set(ch))
    return res


print(solution([2,3,1,4],3))
print(solution([1, 2, 3, 4],5))
print(solution([1, 2, 3, 4],20))
