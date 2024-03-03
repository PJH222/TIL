# https://school.programmers.co.kr/learn/courses/30/lessons/176962#
def solution(plans):
    # 원시적으로 1분씩 지나가는 걸로 새로 만들어 보자
    answer = [] # 답으로 제출할 리스트
    remain = [] # 멈춰둔 과제 리스트

    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        # 분단위 시간으로 변환
        plans[i][1] = plans[i][1].split(":")
        plans[i][1] = int(plans[i][1][0]) * 60 + int(plans[i][1][1])
        plans[i][2] = int(plans[i][2])

    time = plans[0][1] # 현재시각으로 쓸 포인터
    len_plans = len(plans)
    idx = 0

    while len(answer) != len_plans:
        if idx != len(plans) - 1:
            if plans[idx]:
                answer.append(1)

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]	))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))