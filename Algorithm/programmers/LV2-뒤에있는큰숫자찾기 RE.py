def solution(numbers):
    answer = [-1] * len(numbers)
    backnumber = numbers[-1]

    for i in range(len(numbers)-2,-1,-1):
        if numbers[i] >= backnumber:
            backnumber = numbers[i]
            continue
        for j in range(i+1,len(numbers)):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break

            if numbers[i] >= numbers[j] and numbers[i] < answer[j]:
                answer[i] = answer[j]
                break

    # backMax = numbers[-1]
    # 이 방법은 -1걍 다 넣어두고 ,
    # 큰 값이 없다면 내비두고
    # 큰 값이 있으면 새로운 값 넣는 방식,,,
    # print(answer, backMax)
    # for i in range(len(numbers)-2,-1,-1):
    #     if numbers[i] >= backMax:
    #         backMax = numbers[i]
    #         continue
    #     for j in range(i+1,len(numbers)):
    #         if numbers[j] > numbers[i]:
    #             answer[i] = numbers[j]
    #             break
    #         if numbers[i] >= numbers[j] and numbers[i] < answer[j]:
    #             answer[i] = answer[j]
    #             break
    return answer
print(solution([2, 3, 3, 5]	))
print(solution([9, 1, 5, 3, 6, 2]	))