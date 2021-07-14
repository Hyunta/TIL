import heapq

def solution(operations):
    heap = []

    for o in operations:
        oper, num = o.split()
        num = int(num)

        if oper == "I":
            heapq.heappush(heap, num)

        elif heap:
            if num == -1:
                heapq.heappop(heap)
            elif num == 1:
                heap.remove(max(heap))

    print(heap)
    if heap:
        return [max(heap), heapq.heappop(heap)]
    else:
        return [0,0]






print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
