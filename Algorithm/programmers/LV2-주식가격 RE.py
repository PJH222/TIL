# https://school.programmers.co.kr/learn/courses/30/lessons/42584
import heapq

def solution(prices):
    answer = []

    cnt = 0
    diction = {}

    for k,v in enumerate(prices):
        diction[k] = v

    for i in range(len(prices)-1):
        if diction[i] > heapq.heappushpop((list(diction.values())[i:]),1000000):
            pass







    return answer

print(solution([1, 2, 3, 2, 3]	))
