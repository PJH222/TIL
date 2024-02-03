# 우선 3 가지 경우만 신경 쓰면된다는 것
# 2^20 = 1000000이상
# 3^15 = 1000000이상
from itertools import product


from collections import deque
# import sys
# sys.setrecursionlimit(10000)
def solution(x, y, n):
    # 빈 v array 생성
    v = [0] * (y+1)
    # 초기값 설정
    v[x] = 1
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        # y값에 도달한 경우 리턴
        if cur == y:
            return v[y] - 1
        for num in (cur+n, cur*2, cur*3):
            if 0 <= num <= y and v[num] == 0: # 이전에 도달한 적 있으면 빠꾸
                q.append(num)
                # 액션 카운트 +1
                v[num] = v[cur] + 1
        # print(cur,q)
        # print(v)

    return -1


# print(solution(10,40,5))
# print(solution(10,40,30))
# print(solution(2,5,4))
# print(solution(35,148,2))
# print(solution(1,3,2))
# print(solution(1,100,2))
# print(solution(1,10,2))
# print(solution(1,9,2))
# print(solution(2,10,2))
# print(solution(1,30,2))
print(solution(1,1000,1))