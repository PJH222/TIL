from collections import deque

def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)

    q1s = sum(que1)
    q2s = sum(que2)

    limit = len(que1) + len(que2)
    cnt = 0

    while len(que2) != limit:
        while que1 and q1s > q2s:
            tmp = que1.popleft()
            que2.append(tmp)
            q1s -= tmp
            q2s += tmp
            cnt += 1

        if q1s == q2s:
            return cnt

        while que2 and q2s > q1s:
            tmp = que2.popleft()
            que1.append(tmp)
            q2s -= tmp
            q1s += tmp
            cnt += 1

        if q1s == q2s:
            return cnt

        if len(que1) == limit or cnt > limit:
            return -1






    return answer

print(solution([3, 2, 7, 2],	[4, 6, 5, 1]))
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]))
print(solution([1, 1]	,[1, 5]))
print(solution([1, 1]	,[2, 5]))