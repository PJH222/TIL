def solution(land):
    answer = 0
    queue = []
    diction = {}

    for i in range(len(land)-1):
        less1 = sorted(land[i])[-2] # 2번째로 큰 수
        less2 = sorted(land[i+1])[-2]
        # print(less1,less2)
        if land[i].index(max(land[i])) == land[i+1].index(max(land[i+1])):
            if less1 >= less2 and max(land[i]) < max(land[i+1]):
                queue.pop()
                queue.append(less1)
                queue.append(max(land[i+1]))
            if less1 <= less2 and max(land[i]) > max(land[i + 1]):
                queue.append(less1)

        else:
            queue.append(max(land[i]))

    answer = sum(queue)





    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]	))