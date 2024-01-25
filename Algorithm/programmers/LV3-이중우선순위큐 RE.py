import heapq


def solution(operations):
    minheap = []
    maxheap = []
    length = 0
    for oper in operations:
        if length == 0:
            minheap = []
            maxheap = []
        op = oper.split(' ')
        if op[0] == 'I':
            heapq.heappush(minheap, int(op[1]))
            heapq.heappush(maxheap, -int(op[1]))
            length += 1
        elif length > 0:
            length -= 1
            if op[1] == '1':
                heapq.heappop(maxheap)
            else:
                heapq.heappop(minheap)

    if length <= 0:
        return [0, 0]
    else:
        return [-heapq.heappop(maxheap), heapq.heappop(minheap)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))
print(solution(["I " + str(x) for x in range(300000)] + ["D 1", "D -1"] * 1000000 + ["I " + str(x) for x in range(300000, 600000)] + ["D 1", "D -1"] * 1000000	))