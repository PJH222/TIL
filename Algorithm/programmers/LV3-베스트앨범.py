# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dictt = {}
    diction = {}
    sum_diction = {}
    for i in range(len(genres)):
        if genres[i] not in diction:
            diction[genres[i]] = [[plays[i],i]]
            sum_diction[genres[i]] = plays[i]
        else:
            diction[genres[i]] += [[plays[i],i]]
            sum_diction[genres[i]] += plays[i]
    # print(diction)
    a = list(sum_diction.values())
    a.sort(reverse=True) # 크기를 내림차순 정렬

    for i in a:
        for key,val in sum_diction.items():
            if sum_diction[key] == i:
                stack = []
                if len(diction[key]) >= 2:
                    maxx = max(diction[key])
                    stack.append(maxx)
                    diction[key].remove(maxx)
                    maxx = max(diction[key])
                    stack.append(maxx)
                    if stack[0][0] == stack[1][0]:
                        answer.append(stack[1][1])
                        answer.append(stack[0][1])
                    else:
                        answer.append(stack[0][1])
                        answer.append(stack[1][1])
                elif len(diction[key]) == 1:
                    answer.append(diction[key][0][1])
    # print(answer)
    result = []
    # for i in answer:
    #     result.append(i[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"]	,[500, 600, 150, 800, 2500]	))
print(solution(["classic", "pop", "classic", "classic", "pop"]	,[800, 600, 150, 800, 2500]	))
print(solution(["classic", "pop", "classic", "classic"]	,[800, 600, 150, 800]	))