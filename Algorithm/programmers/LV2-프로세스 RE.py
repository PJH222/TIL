# https://school.programmers.co.kr/learn/courses/30/lessons/42587
import heapq

def solution(priorities, location):
    cnt = 0
    answer = 0
    result = [0 for i in range(len(priorities))]
    for i in range(9,0,-1): # 1~9 우선 순위 표시
        if i in priorities:







    return answer

print(solution([2, 1, 3, 2]	, 2))
print(solution([1, 1, 9, 1, 1, 1]	,0))