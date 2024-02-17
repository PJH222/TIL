# https://school.programmers.co.kr/learn/courses/30/lessons/250135

from copy import deepcopy
from collections import deque


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 1) 초/분/시침 모두 겹칠 때

    # 2) 초/시침만 겹칠 때

    # 3) 초/분침만 겹칠 때
    # print(60*60*24) = 86400 아무리 커도 100000이 안됨...
    # for 문 겹치는건 안돼도, 여러개 쓰는 건 가능함

    # 초단위 시간
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2

    angle_s = s1 * 6
    angle_m = m1 * 6 + s1 / 10
    angle_h = h1 * 30 + m1 / 10 + s1 / 600
    a = [angle_h, angle_m, angle_s]  # 시/분/초를 각도로 나타낸 것.
    # print(a)

    aa = []
    # aa = deque()
    print(aa)
    for i in range(start + 1, end - 1):
        b = deepcopy(a)  # 더하기 전의 값

        a[2] += 6  # 1초에 초침이 움직이는 각도
        a[1] += 6 / 60  # 1초에 분침이 움직이는 각도
        a[0] += (6 / 60) / 60  # 1초에 시침이 움직이는 각도

        if a[0] >= 360:
            a[0] -= 360
        if a[1] >= 360:
            a[1] -= 360
        if a[2] >= 360:
            a[2] -= 360

        # b = aa.pop() # 직전 값

        # 시침 분침 초침이 겹치는 시간은 12:00:00 밖에 없다..

        if b[2] <= a[1] and a[2] >= a[1]:  # 분침이 겹친 경우
            answer += 1
            print(a)
        elif b[2] <= a[0] and a[2] >= a[0]:  # 시침이 겹친 경우
            answer += 1
            print(a)
        # aa.append(a)

    # print(b)

    return answer