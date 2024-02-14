import sys
sys.setrecursionlimit(100)

def moving(tmp1, tmp2 ,s1, s2, s3, answer, top, n):
    global result
    # 옮겼던 것을 바로 다시 옮기는 경우를 제외하고 반복하면 되지않을까?
    # print(s1, s2, s3)
    # print(tmp1, tmp2)
    print("현재 탑의 상태",s1,s2,s3, tmp1, tmp2)
    origin = []
    origin.append(len(s1))
    origin.append(len(s2))
    origin.append(len(s3))
    # print(origin)

    # 근데 tmp1을 어떻게 골라야하는거지....?
    if len(s1) > 0 and tmp2 != 1: # 옮긴 위치에서 다시 뺴면 안됨
        plate = s1[-1]
        if len(s2) > 0 and plate < s2[-1] and tmp1 != 2:
            plate = s1.pop()  # 뺀 원반의 위치...
            tmp1 = 1
            s2.append(plate)
            tmp2 = 2
        elif len(s2) == 0:
            plate = s1.pop()  # 뺀 원반의 위치...
            tmp1 = 1
            s2.append(plate)
            tmp2 = 2
        elif len(s3) > 0 and plate < s3[-1] and tmp1 != 3:
            plate = s1.pop()  # 뺀 원반의 위치...
            tmp1 = 1
            s3.append(plate)
            tmp2 = 3
        elif len(s3) == 0:
            plate = s1.pop()  # 뺀 원반의 위치...
            tmp1 = 1
            s3.append(plate)
            tmp2 = 3

        diff = []
        diff.append(len(s1))
        diff.append(len(s2))
        diff.append(len(s3))
        print("변경 후 탑의 상태", s1, s2, s3, tmp1, tmp2)

        # print(origin, diff, tmp1, tmp2)
        if diff != origin:
            answer.append([tmp1, tmp2])
            return moving(tmp1, tmp2 ,s1, s2, s3, answer, top, n)

    if len(s2) > 0 and tmp2 != 2:
        plate = s2[-1]
        if len(s1) > 0 and plate < s1[-1] and tmp1 != 1:
            plate = s2.pop()  # 뺀 원반
            tmp1 = 2
            s2.append(plate)
            tmp2 = 1
        elif len(s1) == 0:
            plate = s2.pop()  # 뺀 원반
            tmp1 = 2
            s2.append(plate)
            tmp2 = 1
        elif len(s3) > 0 and plate < s3[-1] and tmp1 != 3:
            plate = s2.pop()  # 뺀 원반
            tmp1 = 2
            s3.append(plate)
            tmp2 = 3
        elif len(s3) == 0:
            plate = s2.pop()  # 뺀 원반
            tmp1 = 2
            s3.append(plate)
            tmp2 = 3
        diff = []
        diff.append(len(s1))
        diff.append(len(s2))
        diff.append(len(s3))
        print("변경 후 탑의 상태", s1, s2, s3, tmp1, tmp2)

        # print(origin, diff, tmp1, tmp2)
        if diff != origin:
            answer.append([tmp1, tmp2])
            return moving(tmp1, tmp2, s1, s2, s3, answer, top, n)


    if len(s3) > 0 and tmp2 != 3: # 3번째 기둥에서 빼는 경우
        plate = s3[-1]
        if len(s1) > 0 and plate < s1[-1] and tmp1 != 1:
            plate = s3.pop()  # 뺀 원반
            tmp1 = 3
            s1.append(plate)
            tmp2 = 1
        elif len(s1) == 0:
            plate = s3.pop()  # 뺀 원반
            tmp1 = 3
            s1.append(plate)
            tmp2 = 1
        elif len(s2) > 0 and plate < s2[-1] and tmp1 != 2:
            plate = s3.pop()  # 뺀 원반
            tmp1 = 3
            s2.append(plate)
            tmp2 = 2
        elif len(s2) == 0:
            plate = s3.pop()  # 뺀 원반
            tmp1 = 3
            s2.append(plate)
            tmp2 = 2
        diff = []
        diff.append(len(s1))
        diff.append(len(s2))
        diff.append(len(s3))
        print("변경 후 탑의 상태", s1, s2, s3, tmp1, tmp2)

        # print(origin, diff, tmp1, tmp2)

        if diff != origin:
            answer.append([tmp1, tmp2])
            return moving(tmp1, tmp2, s1, s2, s3, answer, top, n)



    if s2 and s2[0] == n: # 가장 바닥이 제일 큰 숫자라면?
        top = 2

    elif s3 and s3[0] == n: # 가장 바닥이 제일 큰 숫자라면?
        top = 3

    answer.append([tmp1, tmp2])
    # print(s1,s2,s3)
    # print(tmp1,tmp2)
    if s2 == result or s3 == result:
        return
    print("끝나벌임...")
    # else:
    #     return moving(tmp1, tmp2 ,s1, s2, s3, answer, top, n)


def solution(n):
    global result, top
    top = 0
    answer = [[]]
    s1, s2, s3 = [i for i in range(n, 0, -1)], [], []
    result = [i for i in range(n, 0, -1)]
    tmp1, tmp2 = 0, 0  # 원반의 원래 위치, 옮긴 원반의 위치
    moving(tmp1, tmp2 ,s1, s2, s3, answer, top, n)

    return answer

print(solution(4))
