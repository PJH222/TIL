# https://school.programmers.co.kr/learn/courses/30/lessons/176962#
from collections import deque


def solution(plans):
    # remain = [aaa , 12:00 , 10]
    # answer = [bbb, ccc , aaa]
    answer = []
    remain = []  # 못하고 남은 과제들의 리스트

    # 보기 좋게 시작 순서대로 정리
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        # 분단위 시간으로 변환
        plans[i][1] = plans[i][1].split(":")
        plans[i][1] = int(plans[i][1][0]) * 60 + int(plans[i][1][1])
        plans[i][2] = int(plans[i][2])

    time = plans[0][1] # 처음 시작 시각
    idx = 0

    len_plans = len(plans) # while 종료 조건

    while len_plans != idx:
        # 5번째를 먼저봐야하는데 remain 확인을 먼저함...
        # print()
        # print("현재 ",idx,"번째 plans의 원소를 보는 중이며,"," 현재시각은 ",time)
        # print(plans)
        # print(remain)
        # print(answer)

        # print(solution([["korean", "11:40", "50"], ["english", "12:10", "50"], ["math", "12:30", "50"]]))
        if idx != len_plans - 1: # 끝에 아직 도달하지 않은 경우
            if len(remain) == 0: # 쟁여놓은게 없는 경우
                if plans[idx][1] + plans[idx][2] <= plans[idx + 1][1]:
                    answer.append(plans[idx][0])
                    time += plans[idx][2]
                    idx += 1

                else:
                    remain.append(plans[idx])
                    remain[-1][2] -= (plans[idx + 1][1] - time)
                    time = plans[idx + 1][1]
                    idx += 1

            # * 쟁여놓은거 먼저 보기, 내가 틀린이유는 쟁여놓은걸 먼저 안봐서 그럼...
            else:
                if time + remain[-1][2] > plans[idx][1]:
                    remain[-1][2] -=  plans[idx][1] - time
                    time = plans[idx][1]
                    # print("집가고싶다아아아")

                if plans[idx][1] + plans[idx][2] <= plans[idx + 1][1]: # 어차피 안될 때,,,
                    answer.append(plans[idx][0])
                    time += plans[idx][2]
                    idx += 1
                    if time + remain[-1][2] <= plans[idx][1]: # 남은 시간동안 잔여과제 처리
                        tmp = remain.pop()
                        time += tmp[2]
                        answer.append(tmp[0])

                    # else:
                    #     remain[-1][2] -= (plans[idx][1] - time)

                else: # 제거 못하는 경우
                    remain.append(plans[idx])
                    remain[-1][2] -= (plans[idx + 1][1] - time)
                    time = plans[idx + 1][1]
                    idx += 1

        # 끝에 도달했을 경우,
        else:
            if len(remain) > 0:
                if time + remain[-1][2] <= plans[idx][1]: # 도달 시간 전인 경우.
                    tmp = remain.pop()
                    time += remain[-1][2]
                    answer.append(tmp[0])
                    # print(23232)
                else: # 다음과제에 도달한 경우 (어차피 마지막 턴이라 시간 줄이고 할 필요가 없음...)
                    remain.append(plans[-1])
                    idx += 1

            else: # 사실 여기서도, answer에 append하거나 remain에 append해도 상관없는 것 같다.
                answer.append(plans[idx][0])
                idx += 1
        # print()
        # print("현재 ", idx, "번째 plans의 원소를 보는 중이며,", " 현재시각은 ", time)
        # print(plans)
        # print(remain)
        # print(answer)

    while remain:
        answer.append(remain.pop()[0])
        # print()
        # print(plans)
        # print(remain)
        # print(answer)

    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]	))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))
print(solution([["music", "11:50", "40"], ["computer", "12:30", "100"], ["science", "12:40", "50"], ["history", "14:00", "30"]]))
# ["music", "science", "history", "computer"]
# print(solution([["korean", "11:40", "50"], ["english", "12:10", "50"], ["math", "12:30", "50"]]))
# ["math", "english", "korean"]
# print(solution([["a","09:00","30"],["b","09:10","20"],["c","09:15","20"],["d","09:55","10"],["e","10:50","5"]]))
# ["c", "b", "d", "a", "e"]
print(solution([["1", "00:00", "30"], ["2", "00:10", "40"], ["3", "00:20", "10"], ["4", "00:25", "10"], ["5", "01:10", "10"]]))
# ["4", "3", "2", "5", "1"]