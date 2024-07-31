def solution(n):
    answer = 1

    for i in range(3,n + 1,2):
        for j in range(2, int(i **0.5) + 1):
            if i % j == 0 and i != j:
                break
        else:
            # print(i, j)
            answer += 1

    print(answer)
    print()
    return answer

solution(10)
solution(5)
solution(1000000)