# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
from collections import deque
from itertools import product



'''
def solution(numbers, target):
    answer = 0
    one_minue = list(product([1,-1],repeat=len(numbers)))

    for one in one_minue:
        # print(one)
        sum = 0
        for i in range(len(numbers)):
            sum += one[i] * numbers[i]
        else:
            if sum == target:
                answer += 1

    return answer
'''

def solution(numbers, target):
    global answer
    answer = 0
    idx = 0
    sum = 0
    def dfs(idx,sum):
        global answer
        if idx == len(numbers):
            if sum == target:
                answer += 1
                return
        else:
            dfs(idx+1, sum + numbers[idx])
            dfs(idx+1, sum - numbers[idx])
    dfs(0,0)
    return answer




print(solution([1, 1, 1, 1, 1],3	))
print(solution([4, 1, 2, 1],4	))