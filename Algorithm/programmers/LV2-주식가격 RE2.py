# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3


def solution(prices):
    times = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        # stack.append((i, prices[i]))
        for idx, price in stack:
            times[idx] += 1 # 남아있는 애들은 1씩 다 더해줄거다~~
        while len(stack) > 0 and stack[-1][1] > prices[i]: # 뒤에 들어온 숫자가 앞숫자보다 작다는 것을 의미,
            stack.pop()
        stack.append((i, prices[i]))
        # print(stack)
    return times



    #
    # for i in range(len(prices)):
    #     for s, idx in stack:
    #         times[idx] += 1
    #     while len(stack) > 0 and stack[-1][0] > prices[i]:
    #         stack.pop()
    #     stack.append((prices[i], i))
    #
    # return times
    #






print(solution([1, 2, 3, 2, 3]	))

