import heapq

def solution(operations):
    cnt = 0
    for i in operations:
        if cnt == 0:
            max_list = []
            min_list = []
        i = i.split(" ")
        if i[0] == "I":
            heapq.heappush(min_list,int(i[1]))
            heapq.heappush(max_list, -int(i[1]))
            cnt += 1
            # print(int(i[1]))

        elif cnt > 0:
            if i[0] == "D":
                if i[1] == '1':
                    heapq.heappop(max_list)
                else:
                    heapq.heappop(min_list)
                cnt -= 1
    if cnt <= 0:
        return [0,0]
    else:
        return [-heapq.heappop(max_list),heapq.heappop(min_list)]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))
# print(solution(["I " + str(x) for x in range(300000)] + ["D 1", "D -1"] * 100000 + ["I " + str(x) for x in range(300000, 600000)] + ["D 1", "D -1"] * 100000	))
print(solution(["I " + str(x) for x in range(30000)] + ["D 1", "D -1"] * 100000 + ["I " + str(x) for x in range(30000, 60000)] + ["D 1", "D -1"] * 100000	))