# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    result = []

    for i in range(len(progresses)):
        cnt = 0
        for j in range(1,101):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                cnt += 1
            else:
                result.append(cnt)
                break

    # print(result)

    for i in range(1,len(result)):
        if result[i-1] > result[i]:
            result[i] = result[i-1]

    for i in result:
        answer.append(result.count(i))
        while result.count(i) > 1:
            result.remove(i)
    # print(result)

    return answer

print(solution([93, 30, 55]	,[1, 30, 5]	 ))
print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	 ))
