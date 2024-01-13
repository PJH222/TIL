# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)

    for _ in range(len(scoville)):
        # print(scoville)
        if len(scoville) >= 2:
            a1 = heapq.heappop(scoville)
            if a1 >= K:
                return answer

            answer += 1
            a2 = heapq.heappop(scoville)
            heapq.heappush(scoville,a1 + a2*2)

        elif len(scoville) == 1:
            if scoville[0] >= K:
                return answer
    return -1



print(solution([3, 2, 3, 4, 10, 12]	,7))
print(solution([12, 2, 3, 9,1, 10, 12]	,7))
print(solution([]	,800))