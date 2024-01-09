# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# dictionary로 구해서 value를 내림차순으로 스택에 k개 만큼 리스트를 만들어서 구하면 될 거 같은데?
# 무슨 귤이 들어가는지는 안궁금함...
def solution(k, tangerine):
    numbers = []
    stack = []
    num_sum = 0
    cnt = 0
    a = len(tangerine)
    b = set(tangerine)
    diction = {}
    # 이 for문이 초과하게 만드는 주범인 것 같은데...
    # 길이와 원소길이 때문에 최소한으로 줄여야함.

    if a == len(b):
        return k

    # 얘가 문제인거 같은데,,,?
    for i in tangerine:
        if i not in diction:
            diction[i] = 1
        else:
            diction[i] += 1

    for i in diction.values():
        numbers.append(i)

    numbers.sort(reverse=True)


    for i in numbers:
        num_sum += i
        cnt += 1
        if num_sum >= k:
            return cnt





print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]	))
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]	))
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]	))
# print(solution(10000,[i for i in range(1000000)]))
