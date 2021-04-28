from collections import deque

def solution(cacheSize, cities):
    tot = 0
    buffer = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city in buffer:
            buffer.remove(city)
            buffer.append(city)
            tot += 1
        else:
            tot += 5
            if len(buffer) == cacheSize:
                buffer.popleft()
            buffer.append(city)
    return tot
    


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))