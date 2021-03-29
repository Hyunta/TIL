def solution(people, limit):
    people.sort()
    cnt = 0
    while people:
        hv = people.pop()
        if people and hv + people[0] <= limit:
            people.pop(0)
            cnt += 1
        else:
            cnt += 1
    return cnt