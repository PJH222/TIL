import time
def solution(n):
    strtrr = time.time()
    cnt, tmp = 0, 0

    end = sum(range(1,n+1))
    all_summ = (1 + end) * end//2

    answer = [0] * end
    diction = {}
    for i in range(len(answer)):
        diction[i] = 0

    cnt = 0
    tmp = 1
    x = 0 # 현재 위치를 표시
    indic = "R"

    check = 0

    while 0 in answer:
        a = diction
        if indic == "R" and x + cnt < len(answer) and diction[x + cnt] == 0: # 오른쪽으로 띄엄띄엄
            diction[x + cnt] = tmp
            x += cnt
            tmp += 1
            cnt += 1

        elif indic == "R" and x + 1 < len(answer) and diction[x + 1] == 0: # 오른쪽으로 엉금엉금
            x += 1
            diction[x] = tmp
            tmp += 1
            if x + 1 == len(answer) or diction[x+1] != 0:
                indic = "L"

        elif indic == "L" and x - cnt >= 0 and diction[x - cnt] == 0: # 왼쪽으로 띄엄띄엄
            x -= cnt
            diction[x] = tmp
            tmp += 1
            cnt -= 1
            if x - cnt == 0:
                indic = "R"

        elif indic == "L" and diction[x - cnt] != 0:
            indic = "R"
            continue
        check += 1

        # print(end, diction)
        # print(indic, x, cnt, tmp)

        b = diction

        # print(check,all_summ)
        if check >= end: # tmp 변동 없으면 멈추기
            break
    answer = []
    for val in diction.values():
        answer += [val]

    return answer

strt1 = time.time()
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(1000))
strt2 = time.time()
# print(strt2-strt1)