import heapq as hq

def solution(jobs):
    answer = 0
    time = 0
    last = -1
    cnt = 0
    h_jobs = []
    while cnt < len(jobs):
        for job in jobs:
            if last < job[0] <= time:
                hq.heappush(h_jobs,[job[1],job[0]])
        if h_jobs:
            cnt += 1
            last = time
            tmp = hq.heappop(h_jobs)
            time += tmp[0]
            answer += time - tmp[1]
        else:
            time += 1
    return answer // cnt