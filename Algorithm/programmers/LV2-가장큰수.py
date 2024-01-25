import itertools

def solution(numbers):
    answer = ''
    result = []
    for i in numbers:
        if 0<= i < 10:
            result.append([i*111,i])
        elif 10<= i < 100:
            result.append([i*10.1,i])
        else:
            result.append([i*1.01,i])

    result.sort(reverse=True)
    # print(result)

    for i in range(len(result)-1):
        if result[i][0] == result[i+1][0]:
            result[i],result[i + 1] = result[i + 1] , result[i]
        answer += str(result[i][1])
    answer += str(result[-1][1])




    return answer if len(answer) != answer.count("0") else "0"

print(solution([6, 10, 2]	))
print(solution([9,90,900,98,901]	))
print(solution([3,33,333,343,34,35,344,340]	))