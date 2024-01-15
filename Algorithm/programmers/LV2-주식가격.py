# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):

        second = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                second += 1

                answer.append(second)
                break
            elif j == len(prices) - 1 and prices[i] > prices[j]:
                answer.append(second)
            elif j == len(prices) - 1 and prices[i] <= prices[j]:
                second += 1
                answer.append(second)
            else:
                second += 1
    answer.append(0)
        # print(second)
    return answer



print(solution([1, 2, 3, 2, 3]	))
