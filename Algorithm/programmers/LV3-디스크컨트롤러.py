# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq
def solution(jobs):
    answer = 0
    x , distance = 0,0
    working = []
    waiting = []
    n = len(jobs)
    while jobs:
        jobs.sort()






        # print(x)
        # answer += x

    # return int(answer//n)

print(solution([[0, 3], [1, 9], [2, 6]]	))
# print(solution(	[[0, 3], [10, 1]]))
# print(solution(	[[7, 8], [3, 5], [9, 6]] ))
# print(solution([[1, 4], [7, 9], [1000, 3]] 	))
# print(solution(	[[0, 1], [2, 2], [2, 3]]))

# x1 = 0 3 9 21 30 /    0, 3-2+6, 3+6-7+12,
# x2 = 0 3 9 18 30
