def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and (numbers[i] + numbers[j]) not in answer:
                answer.append(numbers[i] + numbers[j])
    answer = sorted(answer)
    print(answer)
    return answer


solution([2,1,3,4,1]	)

solution([5,0,2,7]	)