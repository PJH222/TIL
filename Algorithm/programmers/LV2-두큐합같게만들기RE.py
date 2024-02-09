from collections import deque

def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)

    q1s = sum(que1)
    q2s = sum(que2)

    if (q1s + q2s) % 2:
        return -1

    limit = len(queue1) + len(queue2)
    cnt = 0 # 수행 횟수가 상한보다 높으면 break

    while q1s != q2s: # 두 합이 같아지면 break
        if cnt >= limit:
            return -1

        while que1 and q1s > q2s:
            cnt += 1
            tmp = que1.popleft()
            que2.append(tmp)
            q1s -= tmp
            q2s += tmp

        while que2 and q1s < q2s:
            cnt += 1
            tmp = que2.popleft()
            que1.append(tmp)
            q1s += tmp
            q2s -= tmp


        # print(cnt, limit)
        # print(que1,que2)

    return cnt








print(solution([3, 2, 7, 2],	[4, 6, 5, 1]))
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]))
print(solution([1, 1]	,[1, 5]))
print(solution([1, 1]	,[2, 5]))