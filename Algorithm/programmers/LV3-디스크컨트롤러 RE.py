# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq
def solution(jobs):
    answer = 0
    z = len(jobs)
    jobs.sort(key=lambda x:x[1])
    # print(jobs)
    time = 0
    while len(jobs) > 0:
        for job in jobs:
            if job[0] <= time:
                jobs.remove(job)
                # heapq.heappop(jobs)
                time += job[1] - 1
                answer += time - job[0] + 1
                print(time - job[0] + 1, job[1] - 1)
                break
        time += 1
    return answer//z

# def diff()

print(solution([[0, 3], [1, 9], [2, 6]]	))
print(solution([[0, 3],[0,4], [1, 9],[1,8], [2, 6]]	))
print(solution(	[[0, 3], [10, 1]]))
print(solution(	[[7, 8], [3, 5], [9, 6]] ))
print(solution([[0, 4], [0, 9], [1000, 3]] 	))
print(solution(	[[0, 1], [2, 2], [2, 3]]))
