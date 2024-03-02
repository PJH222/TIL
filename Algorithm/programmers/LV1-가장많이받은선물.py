# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    answer = 0
    give = {}  # 준 내역
    receive = {}  # 받은 내역
    present_score = {}  # 선물 지수
    result = {}  # 최종으로 몇개 받거나 줄지

    # dic. 만들기 사전준비
    for i in friends:
        give[i] = [0 for i in range(len(friends))]
        receive[i] = [0 for i in range(len(friends))]
        result[i] = 0
        present_score[i] = 0

    # 받는 숫자, 주는 숫자를 정리한 dic.
    for i in gifts:
        a = i.split(" ")[0]
        b = i.split(" ")[1]
        bb = friends.index(b)
        aa = friends.index(a)

        give[a][bb] += 1
        receive[b][aa] += 1
        present_score[a] += 1
        present_score[b] -= 1

    # 받는 개수만 고려하면 된다.
    stack = []
    for i in friends:
        stack.append(i)
        for j in range(len(friends)):
            if i == friends[j] or friends[j] in stack:
                continue

            a = give[i][j] - receive[i][j]

            if a > 0:
                result[i] += 1

            elif a < 0:
                result[friends[j]] += 1

            else:
                b = present_score[i] - present_score[friends[j]]
                if b > 0:
                    result[i] += 1
                elif b < 0:
                    result[friends[j]] += 1

    for i in result:
        if result[i] > answer:
            answer = result[i]

    return answer